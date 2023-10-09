from typing import List
"""AsyncIO Functions"""

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each call.
    
    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
