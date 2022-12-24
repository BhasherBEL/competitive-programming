from abc import ABC, abstractmethod
from typing import Callable

class SegmentTree(object):
    @abstractmethod
    def __init__(self, arr: list, fn: Callable, default: any=0) -> None:
        pass

    @abstractmethod
    def get(self, i: int, j: int) -> any:
        pass

    @abstractmethod
    def update(self, p: int, v: any) -> None:
        pass
