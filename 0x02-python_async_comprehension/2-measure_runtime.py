#!/usr/bin/env python3
"""Async Comprehension Functions"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the generator function
    Params: None
    Return: A float of seconds
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
