from collections import deque
from typing import Any
from .base import EvictionPolicy

class FIFOEvictionPolicy(EvictionPolicy):    
    def __init__(self):
        self.queue = deque()
        
    def on_put(self, key: Any) -> None:
        self.queue.append(key)
        
    def on_get(self, key: Any) -> None:
        pass
    
    def on_remove(self, key: Any) -> None:
        try:
            self.queue.remove(key)
        except ValueError:
            pass
    
    def evict(self) -> None:
        if self.queue:
            return self.queue.popleft()
        raise Exception("No keys to evict.") 
    
    def reset(self) -> None:
        self.queue.clear()