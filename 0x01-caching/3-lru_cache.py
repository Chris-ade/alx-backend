#!/usr/bin/python3
"""
LRU caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU cache system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializes the LRU Cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.order.remove(key)
                    del self.cache_data[key]
                else:
                    del self.cache_data[self.order.pop(0)]
                print("DISCARD:", self.order[0])
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """
        Retrieves an item from cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
