#!/usr/bin/env python3
""" module for filter_datum function """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function that return a message obfuscated """
    for msj in fields:
        message = re.sub(
            f"(?<={msj}=).*?(?={separator})", redaction, message)
    return message
