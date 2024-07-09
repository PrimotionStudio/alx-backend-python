#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    This function measures the time
    it takes to complete
    """
    start = time.perf_counter()
    result = await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start
    return elapsed
