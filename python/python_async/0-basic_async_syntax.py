#!/usr/bin/env python3
"""Comment"""
import asyncio
import random


async def wait_random(max_delay):
    """Asynchronous function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
