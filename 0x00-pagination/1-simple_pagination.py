#!/usr/bin/env python3
"""
Simple pagination module
"""

import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size should be a positive integer"
        
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
        
        
def index_range(page: int, page_size: int) -> tuple:
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
