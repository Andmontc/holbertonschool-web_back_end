#!/usr/bin/env python3
""" Module that Return measure """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that return a list of random floats """
    rnd_numbers = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(rnd_numbers)
