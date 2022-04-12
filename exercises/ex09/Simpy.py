"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union
from unittest import result

__author__ = "7305-26509"


class Simpy:
    """class for list of floats."""
    values: list[float]

    def __init__(self, num: list[float]):
        """Establish Simpy class."""
        self.values = num
        
    def __str__(self) -> str:
        """Make Simpy a string."""
        return f'Simpy({self.values})'

    def fill(self, num: float, times: int) -> None:
        """Fill Simpy with floats n number of times."""
        self.values = []
        while times != 0:
            self.values.append(num)
            times -= 1
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Range like function for floats."""
        assert step != 0.0
        self.values.append(start)
        defstep = step
        stop -= step
        if step > 0.0:
            while stop > start:
                x = step + start
                self.values.append(x)
                step += defstep
                stop -= defstep
            return None
        else:
            while stop < start:
                x = step + start
                self.values.append(x)
                step += defstep
                stop -= defstep
            return None
    
    def sum(self) -> float:
        """Add the floats in Simpy."""
        i: float = 0.0
        for value in self.values:
            i += value
        return i 

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition operator overload."""
        while isinstance(rhs, Simpy):
            return Simpy([self.values[i] + rhs.values[i] for i in range(len(self.values))])
        while isinstance(rhs, float):
            return Simpy([self.values[i] + rhs for i in range(len(self.values))])

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponent operator overload."""
        if isinstance(rhs, Simpy):
            res_list = []
            for i in range(0, len(self.values)):
                res_list.append(self.values[i] ** rhs.values[i])
            return Simpy(res_list)
        if isinstance(rhs, float):
            return Simpy([self.values[i] ** rhs for i in range(len(self.values))])

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equal operator overload."""
        if isinstance(rhs, Simpy):
            end: list[bool] = []
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    end.append(True)
                else: 
                    end.append(False)
            return end
        
        if isinstance(rhs, float):
            end: list[bool] = []
            for item in self.values:
                if item == rhs:
                    end.append(True)
                else:
                    end.append(False)
            return end
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than operator overload."""
        if isinstance(rhs, Simpy):
            end: list[bool] = []
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    end.append(True)
                else: 
                    end.append(False)
            return end
        
        if isinstance(rhs, float):
            end: list[bool] = []
            for item in self.values:
                if item > rhs:
                    end.append(True)
                else:
                    end.append(False)
            return end
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:  
        """Get item operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            end: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i] is True:
                    end.append(self.values[i])
            return Simpy(end)
    

                    
    
