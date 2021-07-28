#!/usr/bin/env python3
"""
Simple helper function

Classes:
    Server

Functions:
    dataset(object) -> list(list)
    get_page(object, integer, integer) -> list(list)
    index_range(integer, integer) -> tuple(integer, integer)
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function named index_range that takes two integer arguments page
    and page_size

    Parameters:
        page (int): index start number
        page_size (int): index end number

    Returns:
        return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes
    """
    size_tuple_two = ()
    start_index = page
    end_index = page_size
    size_tuple_two = ((end_index * (start_index - 1)), end_index * page)
    return size_tuple_two


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
        NUM_DATASET = 19419
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        page, page_size = index_range(page, page_size)
        with open("file.csv") as csvfile:
            if page > NUM_DATASET or page_size > NUM_DATASET:
                return list()
            datareader = csv.reader(csvfile)
            dataset = []
            line_count = 0
            for row in datareader:
                if line_count == 0:
                    line_count = 1
                    continue
                if page == page_size:
                    break
                dataset.append(row)
                page += 1
        return dataset
