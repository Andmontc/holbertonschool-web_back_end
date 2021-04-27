#!/usr/bin/env python3
""" Module that Return measure """

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Return time measure of a function"""
    initTime = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - initTime) / n
