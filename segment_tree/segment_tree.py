from typing import List, Any
from abc import ABC, abstractmethod


class SegmentTree(ABC):
    def __init__(self, array_list: List[int]) -> None:
        self.t = [0] * (len(array_list) * 4)
        self.a = array_list

    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def __call__(self, l: int, r: int):
        pass

    @abstractmethod
    def update(self, pos: int, new_val: int) -> None:
        pass


class SumSegmentTree(SegmentTree):
    """Segment tree python implementation
    In a nutshell segment tree helps to answer questions about the ranges
    inside of a single list. Formally, the Segment tree is used to build
    queries to find all the possible sum combinations of consegutive elements
    in a list
    Time complexity:
    - O(logn)
    Space complexity
    - O(4n)
    """

    def __build(self, v: int, tl: int, tr: int) -> None:
        if tl == tr:
            self.t[v] = self.a[tl]

        else:
            tm = tl + (tr - tl) // 2
            self.__build(v * 2, tl, tm)
            self.__build(v * 2 + 1, tm + 1, tr)
            self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def build(self) -> None:
        """Build the segment tree"""
        self.__build(1, 0, len(self.a) - 1)

    def __sum(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.t[v]

        tm = tl + (tr - tl) // 2

        return self.__sum(v * 2, tl, tm, l, min(r, tm)) + self.__sum(
            v * 2 + 1, tm + 1, tr, max(l, tm + 1), r
        )

    def __call__(self, l: int, r: int) -> int:
        return self.__sum(1, 0, len(self.a) - 1, l, r)

    def __update(self, v: int, tl: int, tr: int, pos: int, new_val: int) -> None:
        if tl == tr:
            self.t[v] = new_val
        else:
            tm = tl + (tr - tl) // 2
            if pos <= tm:
                self.__update(v * 2, tl, tm, pos, new_val)
            else:
                self.__update(v * 2 + 1, tm + 1, tr, pos, new_val)

            self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def update(self, pos: int, new_val: int) -> None:
        self.a[pos] = new_val
        self.__update(1, 0, len(self.a) - 1, pos, new_val)
