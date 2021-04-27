#!/usr/bin/env python3
""" Module return random number  """


import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ function that measures the total execution time
        for the function wait_n """
    init = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - init) / n
