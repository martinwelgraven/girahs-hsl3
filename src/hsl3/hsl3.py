from typing import Union

from .hsl3_debug_section import Hsl3DebugSection
from .hsl3_generator.configs.module import ConfigModule

class HSL3:
    """A dummy class for the HSL3 logic generator."""

    def __init__(self, name: str):
        """Initialize the HSL3 logic generator."""
        self.name = name
        self.inputs = {}
        self.stores = {}
        self.outputs = {}
        self.timers = {}
        self.config: Union[ConfigModule, None] = None

    def create_debug_section(self):
        debug_section = Hsl3DebugSection()
        return debug_section
    
    def run_in_context(self, callback, params):
        """Run a function in the HSL3 context.
        
        Calls a method in the context of the node. This method is always necessary if data from an external thread is to be called and processed in the context of the node.
        
        Parameters:
        ● callback - Method called in the context of the node.
        ● params - Tuple transferred to the method called as a parameter.
        
        Exceptions:
        ● If no method is transferred for the callback parameter, an exception of the ValueError type is triggered.
        ● If no tuple is transferred for the params parameter, an exception of the ValueError type is triggered.
        """
        callback(*params)
    
    def set_output(self, index_or_key, value):
        """Set an output value in the HSL3 context.

        Sets the specified output to the transferred value. May only be called in the context of the node. If the method is called in a different context/thread, an exception is triggered.
        
        Parameters:
        ● index_or_key - Index or key of the input. If the index or key does not exist, an exception is triggered.
        ● value - Value to be written to the input. Multiple calls in succession overwrite the previous value. Only one value is sent to the output.
        
        Important: The parameter must be of the type float, int or bytes. The HS/FS firmware only supports strings of the type "bytes" within the processing of the logic. De-/encoding may have to be performed by the node itself.
        
        Exceptions:
        ● If the method is not called from the thread of the context, an exception of type Hsl3ContextError is triggered.
        ● If, for the value parameter, None or a "string" type value is transferred, an exception  of the ValueError type is triggered.        
        """
        isfound = False
        if self.config != None:
            for cfg_input in self.config.outputs:
                if cfg_input.identifier == index_or_key:
                    print(f"Output found by key: {index_or_key}")
                    isfound = True
                    break
        
        if isfound == False: raise ValueError(f"Output index or key '{index_or_key}' does not exist.") 
        
        self.outputs[index_or_key] = value
        if isinstance(value, str):
            raise ValueError(f"String values are not allowed. Please encode to bytes before setting the output. Key: {index_or_key}, Value: {value}")
        elif isinstance(value, (bytes, bytearray)):
            display = value.decode("ascii")
        else:
            display=value
        
        print(f"Output set: {index_or_key} = {display}")
    
    def set_store(self, index_or_key, value):
        """Set a store value in the HSL3 context.
        Sets the specified memory variable to the transferred value. May only be called in the context of the node.
        
        Parameters:
        ● index_or_key - Index or key of the memory variable. If the index or key does not exist, an exception is triggered.
        ● value - Value to be written to the memory variable. Must be of the type float, int or bytes, otherwise an exception is triggered.
        
        Important: The parameter must be of the type float, int or bytes. The HS/FS firmware only supports strings of the type "bytes" within the processing of the logic. De-/encoding may have to be performed by the node itself.
        Exceptions:
        
        ● If the method is not called from the thread of the context, an exception of type Hsl3ContextError is triggered.
        ● If, for the value parameter, None or a "string" type value is transferred, an exception of the ValueError type is triggered.
        """
        if isinstance(value, (bytes, bytearray)):
            display = value.decode("iso-8859-15")
        else:
            display = value
        print(f"Store set: {index_or_key} = {display}")

    def set_timer(self, index_or_key, seconds):
        """Set a timer in the HSL3 context.
        Sets a timer with the specified index or key to the transferred time. May only be called in the context of the node.
        
        Parameters:
        ● index_or_key - Index or key of the timer. If the index or key does not exist, an exception is triggered.
        ● seconds - Value in seconds after which the timer is triggered. If the value None or 0 is transferred, the timer is stopped. If an invalid value is transferred, an exception is triggered.
        
        Exceptions:
        ● If the method is not called from the thread of the context, an exception of type Hsl3ContextError is triggered.
        """
        print(f"Timer set: {index_or_key} = {seconds} seconds")
    
    def get_logger(self, host, port, console, level):
        """Generates a logger with which log messages can be sent via Syslog. The HS-specific Syslog server can be reached at the address 127.0.0.1:65002.
        
        Parameters:
        ● host - Hostname or IP address of the Syslog server.
        ● port - Port number of the Syslog server.
        ● console - Boolean indicating whether to also log to the console.
        ● level - Logging level.
        """
        print(f"Logger created: host={host}, port={port}, console={console}, level={level}")

    def get_instance(self, instance_id):         
        """ Returns the instance of an HSL3 node. Parameters:
        ● instance_id - ID of an HSL3 node. The instance must belong to the same context. 
        """
        print(f"Instance returned: {instance_id}")

    def get_context_id(self):

        """ Returns the ID of the current context (string). """
        return "context_id_12345"
    
    def get_instance_id(self):
        """ Returns the ID of the current instance (Int). """
        return 12345
    
    def get_module_id(self):
        """ Returns the ID of the current module (Int). """
        return 12345