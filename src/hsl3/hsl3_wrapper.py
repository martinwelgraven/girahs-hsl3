import os
from typing import Union
from .hsl3_generator.parsers.json import parse_json
from .hsl3_slots import Hsl3Slots
from .hsl3_generator.configs.module import ConfigModule


class Hsl3WrapperNode:

    def __init__(self, root_dir: str, logic_node_name: str, node: object) -> None:
        self.node = node
        self.module: Union[ConfigModule, None] = None

        source_file = f'{root_dir}/src/config_{logic_node_name}.json'
    
        self.inputs = Hsl3Slots("inputs")
        self.outputs = Hsl3Slots("outputs")
        self.stores = Hsl3Slots("stores")

        self.open_config(source_file)
        self._set_inputs()
        self._set_outputs()
        self._set_stores()
        self.node.on_init(self.inputs, self.stores) # type: ignore
    

    def open_config(self, source_file):
        with open(source_file, 'r', encoding='utf-8') as qf:
            content = qf.read()
            _, file_extension = os.path.splitext(source_file)
            file_extension = file_extension.lower()

            if file_extension == '.json':
                self.module =  parse_json(source_file, content)

    def set(self, key, value):
        if key in self.inputs.keys():
            self.inputs.get(key).value = value
        elif key in self.stores.keys():
            self.stores.get(key).value = value
        else:
            raise KeyError(f"Key {key} not found.")
        
        self.node.on_calc(self.inputs) # type: ignore

    def _set_inputs(self):
        for input in self.module.inputs: # type: ignore
            if(isinstance(input.init_value, str)):
                input.init_value = input.init_value.encode("ascii")
            self.inputs.set(input)

    def _set_outputs(self):
        for output in self.module.outputs: # type: ignore
            if(isinstance(output.init_value, str)):
                output.init_value = output.init_value.encode("ascii")
            self.outputs.set(output)

    def _set_stores(self):
        for store in self.module.stores: # type: ignore
            if(isinstance(store.init_value, str)):
                store.init_value = store.init_value.encode("ascii")
            self.stores.set(store)
