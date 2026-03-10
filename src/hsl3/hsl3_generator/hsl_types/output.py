from enum import Enum


class OutputType(Enum):
    NUMBER = 1
    STRING = 2  # always bytes

    def upper(self):
        return self.name
