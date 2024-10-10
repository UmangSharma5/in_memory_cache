from .cache import Cache
from .eviction_policies.fifo import FIFOEvictionPolicy
from .eviction_policies.lru import LRUEvictionPolicy
from .eviction_policies.lifo import LIFOEvictionPolicy
from .eviction_policies.mfu import MFUEvictionPolicy

__all__ = [
    "Cache",
    "FIFOEvictionPolicy",
    "LRUEvictionPolicy",
    "LIFOEvictionPolicy",
    "MFUEvictionPolicy"
]
