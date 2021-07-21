#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async

an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n
times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.

Funtions:
    wait_n(n: int, max_delay: int) -> float:
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays

        Parameters:
            n (int): number
            max_delay (int): other number

        Returns:
            list of all the delays
    """
    delays = []
    spawn = []
    i = 0
    while i < n:
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: delays.append(x.result()))
        spawn.append(task)
        i = i + 1

    for i in spawn:
        await i

    return delays
