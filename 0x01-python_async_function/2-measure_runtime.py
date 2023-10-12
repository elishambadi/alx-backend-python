#!/usr/bin/env python3
"""AsycIO Functions"""

from time import perf_counter
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns total_time / n.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.
    Returns:
        float: The average execution time for each call.
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
