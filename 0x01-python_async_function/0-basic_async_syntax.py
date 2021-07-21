#!/usr/bin/env python3
"""The basics of async

an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay (included and
float value) seconds and eventually returns it.

Function:
    async def wait_random(max_delay: int) -> int:
"""

import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> int:
    """
    return seconds

        Parameters:
            max_delay (int): number of seconds to wait

        Return:
        seconds 
    """
    seconds = time.perf_counter()
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    elapsed = time.perf_counter() - seconds
    return elapsed
