from hsl3.hsl3_generator.hsl_types.output import OutputType
from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class ConfigOutput:
    label: str
    init_value: Union[bytes, float]
    type: OutputType
    index: int = field(init=False)
    identifier: Optional[str] = ''
    _next_id: int = field(default=1, init=False, repr=False)
    
    def __post_init__(self):
        self.index = ConfigOutput._next_id
        ConfigOutput._next_id += 1
        self.type = OutputType[self.type.upper()]