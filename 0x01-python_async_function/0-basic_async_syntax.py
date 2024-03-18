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


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
