#!/usr/bin/env python3
"""
This module contains a basic async function
"""
import random
import asyncio


async def wait_random(max_delay: int | float = 10):
    """
    This function waits for a random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay