from enum import Enum


class InputType(Enum):
    NUMBER = 1
    STRING = 2              # always bytes
    BASE_PATH = 3
    DESTINATION_PORT = 4

    def upper(self):
        return self.name
