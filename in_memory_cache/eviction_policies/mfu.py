from typing import Any, Dict
from .base import EvictionPolicy

# Example of a custom eviction policy: Most Frequently Used (MFU), We can add any policy
class MFUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.frequency: Dict[Any, int] = {}
        
    def on_put(self, key: Any) -> None:
        self.frequency[key] = 1
        
    def on_get(self, key: Any) -> None:
        if key in self.frequency:
            self.frequency[key] += 1
    
    def on_remove(self, key: Any) -> None:
        if key in self.frequency:
            del self.frequency[key]
            
    def evict(self) -> None:
        if not self.frequency:
            raise Exception("No keys to evict.")        
        evict_key = max(self.frequency, key=lambda k: self.frequency[k])
        return evict_key
    
    def reset(self) -> None:
        self.frequency.clear()