#!/usr/bin/env python3
""" duck-typed annotations """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element of list or None
    Args:
        lst (Sequence[Any]): a sequence.
    Returns:
        Union[Any, None]: None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
