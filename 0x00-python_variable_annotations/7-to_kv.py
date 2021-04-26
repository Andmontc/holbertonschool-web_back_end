#!/usr/bin/env python3
""" Module that returns the sum of a list """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple with a string and int/float square """
    return (k, (v * v))
