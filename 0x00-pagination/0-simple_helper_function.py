#!/usr/bin/env python3
""" 
Helper function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes
    for a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
