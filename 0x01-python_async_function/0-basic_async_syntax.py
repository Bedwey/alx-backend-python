#!/usr/bin/env python3

"""
This module contains a coroutine that waits for a random delay.

Modules:
    asyncio: This module is used for writing single-threaded concurrent code 
    using coroutines, multiplexing I/O access over sockets and other resources, 
    running network clients and servers, and other related primitives.

    random: This module implements pseudo-random number generators for various 
    distributions including integer and float. In this script, it is used to 
    generate a random float for the delay time.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay the function waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
