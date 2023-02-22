#!/usr/bin/python3
"""
Defines the LIFOCache class that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize LIFOCache object
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in self.cache_data:
            last_key = self.keys.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
