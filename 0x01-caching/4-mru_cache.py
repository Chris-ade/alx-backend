#!/usr/bin/python3
"""MRU Cache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache Class """

    def __init__(self):
        """ Initializes the MRU Cache """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.mru_keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_keys.pop(-2)
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.mru_keys.remove(key)
        self.mru_keys.append(key)

        return self.cache_data[key]
