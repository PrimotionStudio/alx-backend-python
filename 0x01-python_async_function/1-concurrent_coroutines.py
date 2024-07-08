#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function waits for n random numbers between 0 and max_delay
    """
    coroutines: [float] = [wait_random(max_delay) for _ in range(n)]
    res: float = await asyncio.gather(*coroutines)
    return sorted(res)
