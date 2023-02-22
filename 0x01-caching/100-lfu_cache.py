#!/usr/bin/python3
""" LFU Cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.freq_count = {}
        self.min_freq = 0

    def get(self, key):
        """ Return value linked to key """
        if key is None or key not in self.cache_data:
            return None

        # update frequency count for key
        value, freq = self.cache_data[key]
        self.freq_count[key] += 1
        if freq == self.min_freq and len(self.freq_count) > 1:
            self.min_freq = min(self.freq_count.values())

        return value

    def put(self, key, item):
        """ Add key and value to cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # update existing key
            value, freq = self.cache_data[key]
            self.cache_data[key] = (item, freq)
            self.freq_count[key] += 1
            if freq == self.min_freq and len(self.freq_count) > 1:
                self.min_freq = min(self.freq_count.values())
        else:
            # add new key
            if len(self.cache_data) >= self.MAX_ITEMS:
                # discard LFU item(s)
                discard_keys = [k for k in self.freq_count if self.freq_count[k] == self.min_freq]
                if len(discard_keys) > 1:
                    lru_key = min(self.access_time, key=lambda k: self.access_time[k])
                    discard_keys.remove(lru_key)
                for k in discard_keys:
                    del self.cache_data[k]
                    del self.freq_count[k]
                    del self.access_time[k]
                    print("DISCARD:", k)

                self.min_freq += 1

            self.cache_data[key] = (item, 1)
            self.freq_count[key] = 1
            self.access_time[key] = self.current_time
            self.current_time += 1
