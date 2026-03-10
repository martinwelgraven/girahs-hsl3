from typing import Union
from hsl3.hsl3_generator.configs.input import ConfigInput
from hsl3.hsl3_generator.configs.output import ConfigOutput
from hsl3.hsl3_generator.configs.store import ConfigStore
from hsl3.hsl3_generator.configs.timer import ConfigTimer
from hsl3.hsl3_slot import Hsl3Slot

class Hsl3Slots:
    """Instances of this class are transferred when the following methods are called:
    ● on_init(inputs: Hsl3Slots, store: Hsl3Slots)
        ○ inputs - Contains all inputs
        ○ store - Contains all memory variables
    ● on_calc(inputs: Hsl3Slots)
        ○ inputs - Contains all inputs
    ● on_timer(timer: Hsl3Slots)
        ○ timer - Contains all defined timers
    An instance of the Hsl3Slots class can be accessed directly via the index or key of the individual slot.
    Example:
    def on_init(self, inputs, store):
        # Returns instance of Hsl3Slot
        slot_e1 = inputs[1]
        # Returns the value of Input 1
        slot_e1_wert = inputs[1].value
    def on_calc(self, inputs):
        # Retrieves the value from Input 1
        if inputs[1].changed:
            slot_e1_wert = inputs[1].value
    """

    def __init__(self, name: str):
        self.name = name
        self._slots_by_key: dict[str, Hsl3Slot] = {}
        self._slots_by_id: list[Union[Hsl3Slot, None]] = [None]  # index 0 unused
        self._meta_by_key: dict[str, object] = {}          # optional: keep ConfigInput/Output/...


    def set(self, init_slot: Union[ConfigInput, ConfigOutput, ConfigStore, ConfigTimer]):
        """
        Sets an object of type Hsl3Slot
        """
        slot = Hsl3Slot()

        idx = int(init_slot.index)  # must be 1..n
        while len(self._slots_by_id) <= idx:
            self._slots_by_id.append(None)
        self._slots_by_id[idx] = slot

        if isinstance(init_slot, (ConfigInput, ConfigOutput, ConfigStore)):
            data_type = init_slot.type.name
            if data_type == "NUMBER":
                if isinstance(init_slot.init_value, bytes) and init_slot.init_value.find(b".")>-1:
                    data_type = "FLOAT"
                else:
                    data_type = "INT"

            slot.data_type = data_type.lower()
            slot.value = init_slot.init_value
        
        if init_slot.identifier:
            self._slots_by_key[str(init_slot.identifier.upper())] = slot
            self._meta_by_key[str(init_slot.identifier.upper())] = init_slot

    def get(self, index_or_key: Union[int, str]) -> Hsl3Slot:
        """Parameters
        ● index_or_key
        
        Return:
        Returns an object of type Hsl3Slot or triggers an exception if the index or key does not exist."""

        if isinstance(index_or_key, int):
            if index_or_key <= 0 or index_or_key >= len(self._slots_by_id):
                raise KeyError(f"Index {index_or_key} not found.")
            slot = self._slots_by_id[index_or_key]
            if slot is None:
                raise KeyError(f"Index {index_or_key} not found.")
            return slot

        key = str(index_or_key)
        try:
            return self._slots_by_key[key]
        except KeyError:
            raise KeyError(f"Key {key} not found.")

    def __getitem__(self, index_or_key: Union[int, str]) -> Hsl3Slot:
        return self.get(index_or_key)
    
    def keys(self):        
        """Returns a list of all existing keys."""
        out = {}
        for i in range(1, len(self._slots_by_id)):
            if self._slots_by_id[i] is not None:    
                out[i] = self._slots_by_id[i]
        for key in self._slots_by_key.keys():
            out[key] = self._slots_by_key[key]

        return out.keys()
    
    def changed(self, index_or_key):
        """Parameters
        ● index_or_key
        
        Return:
        Returns True when a value is received. If no value was received at this input or no value was found for the transferred key, False is returned."""
        slot = self.get(index_or_key)
        if slot is not None:
            return slot.changed
        else:
            raise KeyError(f"Key {index_or_key} not found.")

    def value(self, index_or_key):
        """Parameters
        ● index_or_key
        
        Return:
        Returns the value. If the corresponding index or key is not found, None is returned."""
       

        slot = self.get(index_or_key)
        if slot is not None:
            return slot.value
        else:
            raise KeyError(f"Key {index_or_key} not found.")
