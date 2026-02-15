from types.store import StoreType
from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class ConfigStore:
    label: str
    init_value: Union[str, float]
    type: StoreType
    index: int = field(init=False)
    identifier: Optional[str] = ''
    _next_id: int = field(default=1, init=False, repr=False)
    
    def __post_init__(self):
        self.index = ConfigStore._next_id
        ConfigStore._next_id += 1
        self.type = StoreType[self.type.upper()]