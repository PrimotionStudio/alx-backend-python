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
    waits: [float] = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*waits)
    return merge_sort(results)

def merge_sort(arr):
    """
    This function sorts the array
    """
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    This function merges the two sorted arrays
    """
    sorted_list = []
    left_index, right_index = 0, 0
    
    # Merge the two lists while maintaining the order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements
    if left_index < len(left):
        sorted_list.extend(left[left_index:])
    if right_index < len(right):
        sorted_list.extend(right[right_index:])
    
    return sorted_list