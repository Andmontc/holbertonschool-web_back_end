#!/usr/bin/env python3
""" Module that returns the um of a list """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function that returns the sum of a list
      mxd_lst: list of numbers
    Return: the sum """
    return sum(mxd_lst)
