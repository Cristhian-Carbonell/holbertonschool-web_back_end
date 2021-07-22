#!/usr/bin/env python3
"""
Measure the runtime

Functions:
    def measure_time(n: int, max_delay: int) -> float:
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total_time / n

    measures the total execution time for wait_n

        Parameters:
            n (int): number
            max_delay (int): other number

        Returns:
            total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
