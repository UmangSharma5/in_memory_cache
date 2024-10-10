
# In-Memory Caching Library

## Overview

This in-memory caching library is designed to support multiple eviction policies, enabling the efficient management of a cache of key-value pairs. The cache uses various eviction strategies to determine which elements to remove when the cache exceeds its capacity.

The key features of the library are:
- **Multiple Eviction Policies**: FIFO, LRU, LIFO.
- **Thread Safety**: Ensures that the cache can be accessed and modified safely in a multithreaded environment.
- **Configurable Capacity**: You can set the maximum number of items the cache can store.
- **Custom Eviction Policies**: Option to implement custom eviction policies by extending the provided framework.

## Eviction Policies

The library supports the following built-in eviction policies:

### 1. First-In-First-Out (FIFO)
- Evicts the item that was added to the cache earliest.
- When the cache reaches its capacity, the oldest inserted item is removed to make space for the new one.

### 2. Least Recently Used (LRU)
- Evicts the least recently accessed item.
- If the cache is full, the item that has not been accessed for the longest time will be removed to make space for a new one.

### 3. Last-In-First-Out (LIFO)
- Evicts the most recently added item.
- When the cache is full, the most recently inserted item is removed first.

### 4. Most Frequently Used (MFU)
- Evicts the most used item.
- When the cache is full, the most used item is removed first.


## Running the Code

- The `main.py` file holds a sample test case to demonstrate the use of the cache and eviction policies.
- You can run the code by executing the following command from the terminal in the project directory:

```bash
python3 main.py
```







