#!/usr/bin/env python3
"""Async Comprehension Functions"""

import asyncio
import random


async def async_generator():
    """
    Generates random numbers async, every 1 second
    Params: None
    Return: A random number range 1-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
