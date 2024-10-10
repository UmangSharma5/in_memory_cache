from abc import ABC, abstractmethod
from typing import Any

class EvictionPolicy(ABC):    
    @abstractmethod
    def on_put(self, key: Any) -> None:
        pass
    
    @abstractmethod
    def on_get(self, key: Any) -> None:
        pass
    
    @abstractmethod
    def on_remove(self, key: Any) -> None:
        pass
    
    @abstractmethod
    def evict(self) -> None:
        pass
    
    @abstractmethod
    def reset(self) -> None:
        pass