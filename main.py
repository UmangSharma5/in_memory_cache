from in_memory_cache import Cache, LRUEvictionPolicy, FIFOEvictionPolicy, MFUEvictionPolicy

def main():
    # Initialize LRU Eviction Policy
    lru_policy = LRUEvictionPolicy()
    cache = Cache(capacity=3, eviction_policy=lru_policy)

    # Add items to the cache
    cache.put('A', 1)
    cache.put('B', 2)
    cache.put('C', 3)
    print(cache)  # Cache(capacity=3, size=3, items={'A': 1, 'B': 2, 'C': 3})

    # Access some items
    cache.get('A')  # Access 'A', now 'B' is LRU
    cache.put('D', 4)  # Should evict 'B'
    print(cache)  # Cache(capacity=3, size=3, items={'A': 1, 'C': 3, 'D': 4})

    # Clear the cache
    cache.clear()
    print(cache)  # Cache(capacity=3, size=0, items={})

    # Switch to FIFO Eviction Policy
    fifo_policy = FIFOEvictionPolicy()
    cache.set_eviction_policy(fifo_policy)

    cache.put('E', 5)
    cache.put('F', 6)
    cache.put('G', 7)
    print(cache)  # Cache(capacity=3, size=3, items={'E': 5, 'F': 6, 'G': 7})

    # Clear the cache again
    cache.clear()
    print(cache)  # Cache(capacity=3, size=0, items={})

    # Use custom MFU Eviction Policy
    mfu_policy = MFUEvictionPolicy()
    cache.set_eviction_policy(mfu_policy)

    cache.put('H', 8)
    cache.put('I', 9)
    cache.put('J', 10)
    cache.get('H')  # Frequency of 'H' becomes 2
    cache.get('H')  # Frequency of 'H' becomes 3
    cache.get('I')  # Frequency of 'I' becomes 2
    cache.put('K', 11)  # Should evict 'H' since it has the highest frequency
    print(cache)  # Cache(capacity=3, size=3, items={'I': 9, 'J': 10, 'K': 11})

    # Clear the cache once more
    cache.clear()
    print(cache)  # Cache(capacity=3, size=0, items={})

if __name__ == "__main__":
    main()
