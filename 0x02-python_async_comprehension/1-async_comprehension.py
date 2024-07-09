#!/usr/bin/env python3
"""
This script is used to generate
a list of all the files in a directory
"""
import asyncio
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    This function is used to generate
    a list of all the files in a directory
    """
    return [i async for i in async_generator()]
