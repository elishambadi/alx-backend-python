#!/usr/bin/env python3
"""Async Comprehension Functions"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generates a list every 1 second
    Params: None
    Return: A list of floats from the async generator
    """
    return [x async for x in async_generator()]
