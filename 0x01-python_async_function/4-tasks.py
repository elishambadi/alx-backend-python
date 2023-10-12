#!/usr/bin/env python3
"""AsyncIO Functions"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs task_wait_random n times Asynch with the specified max_delay.
    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds for each call.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    return sorted([task.result() for task in tasks])
