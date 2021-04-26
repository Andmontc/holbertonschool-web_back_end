#!/usr/bin/env python3
""" Module that returns a multiplication """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function callable"""
    return lambda num: multiplier * num
