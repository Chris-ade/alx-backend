#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A basic caching system that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
