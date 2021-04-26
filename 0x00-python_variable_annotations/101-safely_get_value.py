#!/usr/bin/env python3
""" return dict """

from typing import Mapping, Any, Union, T


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Gets value safely.
    Args:
        dct (Mapping): dictionary
        key (Any): a key
        default (Union[T, None], optional): default value. Defaults to None.
    Returns:
        Union[Any, T]: value in key position of dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
