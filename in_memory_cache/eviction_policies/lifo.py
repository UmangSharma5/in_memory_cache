from collections import deque
from typing import Any
from .base import EvictionPolicy

class LIFOEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.stack = deque()
        
    def on_put(self, key: Any) -> None:
        self.stack.append(key)
    
    def on_get(self, key: Any) -> None:
        pass
    
    def on_remove(self, key: Any) -> None:
        try:
            self.stack.remove(key)
        except ValueError:
            pass
    
    def evict(self) -> None:
        if self.stack:
            return self.stack.pop()
        raise Exception("No keys to evict.")
    
    def reset(self) -> None:
        self.stack.clear()