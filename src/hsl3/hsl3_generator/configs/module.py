from dataclasses import dataclass, field
from typing import List, Optional
import datetime
from hsl3.hsl3_generator.configs.output import ConfigOutput
from hsl3.hsl3_generator.configs.input import ConfigInput
from hsl3.hsl3_generator.configs.store import ConfigStore
from hsl3.hsl3_generator.configs.timer import ConfigTimer
from hsl3.hsl3_generator.configs.script import ConfigScript
from hsl3.hsl3_generator.configs.translation import ConfigTranslation

@dataclass
class ConfigModule:
    category: str
    context: str
    id: str
    name: str
    
    inputs: List[ConfigInput]
    outputs: List[ConfigOutput]
    scripts: List[ConfigScript]
    stores: List[ConfigStore] = field(default_factory=list)
    timers: List[ConfigTimer] = field(default_factory=list)
    translations: List[ConfigTranslation] = field(default_factory=list)
    
    version: Optional[str] = datetime.datetime.now().strftime('%y%m%d')
    hsl_filename: Optional[str] = ''
    
    def __post_init__(self):
        if len(str(self.hsl_filename)) == 0:
            self.hsl_filename = f'{self.id}_{self.name}.hsl'