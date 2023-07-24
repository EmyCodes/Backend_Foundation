#!/usr/bin/env python3
"""Comment"""
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
