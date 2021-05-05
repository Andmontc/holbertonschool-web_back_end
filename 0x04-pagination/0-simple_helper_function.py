#!/usr/bin/env python3
""" module for a helper """


def index_range(page, page_size) -> tuple:
    """ Helper function """

    pages = page_size * page

    return ((pages - page_size), pages)
