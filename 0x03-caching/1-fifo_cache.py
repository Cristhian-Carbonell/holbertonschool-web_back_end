#!/usr/bin/env python3
"""FIFO caching

Classes:
    FIFOCache

Functions_
    put(object, key: string, item: string) -> dictionary
    get(object, key: string) -> string
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system

    ...

    Attributes
    ----------
    None

    Methods
    -------
    put(key, item)
        assigns the dictionary cache_data the value of the item for the key

    get(key)
        returns the dictionary cache_data value of the given key
    """
    index = 0

    def __init__(self):
        """
        Constructs all the necessary attributes for the person object
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the dictionary cache_data the value of the item for the key

        If the argument key or item is None, this method should not do anything

        Parameters
        ----------
            key (string): key to append to dictionary
            item (string): value to add the dictionary with its
            corresponding key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    for value in range(len(self.cache_data)):
                        for keys in self.cache_data:
                            if value == FIFOCache.index:
                                self.cache_data.pop(keys)
                                break

                    FIFOCache.index += 1
            if FIFOCache.index == 3:
                FIFOCache.index = 0

    def get(self, key):
        """
        Returns the dictionary cache_data value of the given key

        if the argument key is None or the key doesn't exist in
        dictionary cache_data, return None

        Parameters
        ----------
            key (string): key that will be searched in the dictionary
            to return the value

        Returns
        -------
            Dictionary value if it finds the key, if not none
        """
        string_value = None
        if key is None or key in self.cache_data:
            for keys, values in self.cache_data.items():
                if key == keys:
                    string_value = values

        return string_value
