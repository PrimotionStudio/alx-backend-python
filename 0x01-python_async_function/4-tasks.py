#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function waits for n random numbers between 0 and max_delay
    """
    coroutines: [float] = [task_wait_random(max_delay) for _ in range(n)]
    res: float = await asyncio.gather(*coroutines)
    return sorted(res)
