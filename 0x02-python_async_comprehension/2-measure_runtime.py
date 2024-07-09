#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function measures the time
    it takes to complete
    """
    start: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
