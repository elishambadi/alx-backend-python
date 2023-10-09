#!/usr/bin/env python3
"""Async functions"""

import asyncio
import random
import time


async def wait_random(max_delay: int = 10):
    """Runs an async routine"""
    time.sleep(random.randint(0, max_delay))
    return max_delay

if __name__ == "__main__":
    asyncio.run(wait_random())
