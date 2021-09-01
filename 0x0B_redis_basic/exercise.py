#!/usr/bin/env python3
"""exercise module
"""
import redis
import uuid
from typing import Any


class Cache:
    """Cache class
    """
    def __init__(self):
        """constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
