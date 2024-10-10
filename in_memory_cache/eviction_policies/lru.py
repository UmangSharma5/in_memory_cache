from collections import deque
from typing import Any
from .base import EvictionPolicy

class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.order =  deque()
        
    def on_put(self, key: Any) -> None:
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        
    def on_get(self, key: Any) -> None:
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
    
    def on_remove(self, key: Any) -> None:
        try:
            self.order.remove(key)
        except ValueError:
            pass
    
    def evict(self) -> None:
        if self.order:
            return self.order.popleft()
        raise Exception("No keys to evict.") 
    
    def reset(self) -> None:
        self.order.clear()