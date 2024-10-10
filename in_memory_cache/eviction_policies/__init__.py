from .fifo import FIFOEvictionPolicy
from .lru import LRUEvictionPolicy
from .lifo import LIFOEvictionPolicy
from .mfu import MFUEvictionPolicy
from .base import EvictionPolicy

__all__ = [
    "FIFOEvictionPolicy",
    "LRUEvictionPolicy",
    "LIFOEvictionPolicy",
    "MFUEvictionPolicy",
    "EvictionPolicy"
]
