from abc import ABC, abstractmethod
from typing import Tuple

class KDTree(ABC):
    @abstractmethod
    def __init__(self, vs: list[tuple]) -> None:
        pass

    @abstractmethod
    def nn(self, other: tuple) -> Tuple[tuple, int]:
        pass

    @abstractmethod
    def knn(self, other: tuple, k: int) -> list[Tuple[tuple, int]]:
        pass