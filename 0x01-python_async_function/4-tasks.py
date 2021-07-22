#!/usr/bin/env python3
"""task 4
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
        spawn.append(task)
        i = i + 1

    for i in spawn:
        await i

    return delays
