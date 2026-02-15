import json

from configs.module import ConfigModule
from configs.output import ConfigOutput
from configs.input import ConfigInput
from configs.store import ConfigStore
from configs.timer import ConfigTimer
from configs.script import ConfigScript
from configs.translation import ConfigTranslation

def parse_json(file_content):
    root = json.loads(file_content)
    inputs = []
    outputs = []
    stores = []
    timers = []
    scripts = []
    
    translations = []
    
    for elem in root['module']['inputs']:
        list_item = ConfigInput(**elem)
        inputs.append(list_item)
    
    for elem in root['module']['outputs']:
        list_item = ConfigOutput(**elem)
        outputs.append(list_item)
    
    if 'stores' in root['module']:
        for elem in root['module']['stores']:
            list_item = ConfigStore(**elem)
            stores.append(list_item)
    
    if 'timers' in root['module']:
        for elem in root['module']['timers']:
            list_item = ConfigTimer(**elem)
            timers.append(list_item)
    
    for elem in root['module']['scripts']:
        list_item = ConfigScript(**elem)
        scripts.append(list_item)
    
    if 'translations' in root['module']:
        for elem in root['module']['translations']:
            translation_inputs = []
            
            for ti in elem['translation_inputs']:
                translation_inputs.append(ti['label'])
            translation_outputs = []
            
            for to in elem['translation_outputs']:
                translation_outputs.append(to['label'])
            
            elem_dict = dict(elem)
            elem_dict['translation_inputs'] = translation_inputs
            elem_dict['translation_outputs'] = translation_outputs
            
            list_item = ConfigTranslation(**elem_dict)
            translations.append(list_item)
    
    root['module']['inputs'] = inputs
    root['module']['outputs'] = outputs
    root['module']['stores'] = stores
    root['module']['timers'] = timers
    root['module']['scripts'] = scripts
    root['module']['translations'] = translations

    return ConfigModule(**root['module'])