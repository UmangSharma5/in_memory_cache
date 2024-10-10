import threading
from typing import Any, Dict, Optional
from .eviction_policies.base import EvictionPolicy


class Cache:        
    def __init__(self, capacity: int, eviction_policy: EvictionPolicy):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.cache : Dict[Any, Any] = {}
        self.eviction_policy = eviction_policy
        self.lock = threading.Lock()
        
    def get(self, key: Any) -> Optional[Any]:
        with self.lock:
            if key in self.cache:
                self.eviction_policy.on_get(key)
                return self.cache[key]
            return None
        
    def put(self, key: Any, value: Any) -> None:
        with self.lock:
            if key in self.cache:
                self.cache[key] = value
                self.eviction_policy.on_get(key)
            else:
                if len(self.cache) >= self.capacity:
                    evict_key = self.eviction_policy.evict()
                    if evict_key is not None:
                        del self.cache[evict_key]
                        self.eviction_policy.on_remove(evict_key)
                
                self.cache[key] = value
                self.eviction_policy.on_put(key)
                
    def remove(self, key: Any) -> None:
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                self.eviction_policy.on_remove(key)

    def clear(self) -> None:
        with self.lock:
            self.cache.clear()
            self.eviction_policy.reset()            
            
    def size(self) -> int:
        with self.lock:
            return len(self.cache)
        
    def __repr__(self):
        with self.lock:
            return f"Cache(capacity={self.capacity}, size={len(self.cache)}, items={self.cache})"
        
    def set_eviction_policy(self, eviction_policy: EvictionPolicy) -> None:
        """
        Allows changing the eviction policy. Existing cache keys will be reprocessed.
        """              
        with self.lock:
            new_policy = eviction_policy
            for key in self.cache.keys():
                new_policy.put_on(key)
            self.eviction_policy = new_policy
            


            
            
    
        
    