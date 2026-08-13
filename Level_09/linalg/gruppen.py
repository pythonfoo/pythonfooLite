from abc import ABC, abstractmethod
from typing import Optional

class Gruppe(ABC):
    neutral = None # type: Optional[Gruppe]
    
    @abstractmethod
    def __init__(self, value: "Gruppe") -> None:
        pass
    
    @abstractmethod
    def __mul__(self, other: "Gruppe") -> "Gruppe":
        pass
    
    @abstractmethod
    def __inv__(self) -> "Gruppe":
        pass

class Z_plus(Gruppe):
    neutral = Z_plus(0)
    
    def __init__(self, value: int) -> None:
        assert isinstance(value, int)
        self.value = value
    
    def __mul__(self, other: Z_plus) -> Z_plus:
        assert isinstance(other, Z_plus)
        return Z_plus(self.value + other.value)
    
    def __inv__(self) -> Z_plus:
        return Z_plus(-self.value)
