#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    This function waits for n random numbers between 0 and max_delay
    """
    # coroutines: [float] = [wait_random(max_delay) for _ in range(n)]
    # return sorted(await asyncio.gather(*coroutines))
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Gather all the results
    results = await asyncio.gather(*tasks)
    
    # Insert the results in a way that avoids sorting the entire list
    delays = []
    for result in results:
        # Find the position where to insert the result to maintain ascending order
        i = 0
        while i < len(delays) and delays[i] < result:
            i += 1
        delays.insert(i, result)
    
    return delays