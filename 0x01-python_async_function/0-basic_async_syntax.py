#!/usr/bin/env python3
"""Async functions"""

import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """Runs an async routine"""
    sleep_time = random.random() * max_delay
    time.sleep(sleep_time)
    return sleep_time

if __name__ == "__main__":
    asyncio.run(wait_random())
