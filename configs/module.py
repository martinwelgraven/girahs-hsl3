from dataclasses import dataclass
from typing import List, Optional
import datetime
from configs.output import ConfigOutput
from configs.input import ConfigInput
from configs.store import ConfigStore
from configs.timer import ConfigTimer
from configs.script import ConfigScript
from configs.translation import ConfigTranslation

@dataclass
class ConfigModule:
    category: str
    context: str
    id: str
    name: str
    
    inputs: List[ConfigInput]
    outputs: List[ConfigOutput]
    scripts: List[ConfigScript]
    stores: List[ConfigStore] = []
    timers: List[ConfigTimer] = []
    translations: List[ConfigTranslation] = []
    
    version: Optional[str] = datetime.datetime.now().strftime('%y%m%d')
    hsl_filename: Optional[str] = ''
    
    def __post_init__(self):
        if len(str(self.hsl_filename)) == 0:
            self.hsl_filename = f'{self.id}_{self.name}.hsl'