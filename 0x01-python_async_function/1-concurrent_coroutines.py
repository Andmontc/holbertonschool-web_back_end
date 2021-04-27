#!/usr/bin/env python3
""" Module return random number  """


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that return a list of random floats """
    rnd_numbers = [await wait_random(max_delay) for _ in range(n)]
    return sorted(rnd_numbers)
