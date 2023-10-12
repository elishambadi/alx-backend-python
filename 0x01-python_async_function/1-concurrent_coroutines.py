#!/usr/bin/env python3
"""AsyncIO Functions"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs wait_random n times asynch with the specified max_delay.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.
    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
