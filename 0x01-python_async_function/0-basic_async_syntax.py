#!/usr/bin/env python3
""" Module return random number  """

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function that return a random number with asyncio """
    rand_number = random() * max_delay
    await asyncio.sleep(rand_number)
    return rand_number
