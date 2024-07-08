#!/usr/bin/env python3
"""
This module contains a basic async function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
