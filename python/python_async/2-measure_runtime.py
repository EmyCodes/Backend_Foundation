#!/usr/bin/env python3
"""Comment"""
import asyncio
# from typing import float
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken
