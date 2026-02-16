from enum import Enum


class StoreType(Enum):
    NUMBER = 1
    STRING = 2

    # TODO: UPPER NEEDS TO BE REMOVED, ONLY TO TEMPORARILY SUPPORT ERROR FIXING
    def upper(self):
        return self.name
