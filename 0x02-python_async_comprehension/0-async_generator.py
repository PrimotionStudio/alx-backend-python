#!/usr/bin/env python3
"""
This module contains the function
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This function returns a random number between 0 and 10
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)