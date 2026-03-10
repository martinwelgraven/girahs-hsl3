from hsl3.hsl3_generator.hsl_types.input import InputType
from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class ConfigInput:
    label: str
    init_value: Union[bytes, float]
    type: InputType
    index: int = field(init=False)
    identifier: Optional[str] = ''
    _next_id: int = field(default=1, init=False, repr=False)
    
    def __post_init__(self):
        self.index = ConfigInput._next_id
        ConfigInput._next_id += 1
        self.type = InputType[self.type.upper()]