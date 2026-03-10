class LogicModule:
    def __init__(self, hsl3):
        self.fw = hsl3
        self.debug = self.fw.create_debug_section()
        self.input_values = []

    def on_init(self, inputs, store):
        self.debug.log(f"Called on_init with keys: {inputs.keys()}")
        self.input_values.append(inputs.value("input_1"))
        self.input_values.append(inputs.value("input_2"))
        self.fw.set_output("instance_id_for_clients", self.fw.get_instance_id())

    def on_calc(self, inputs):
        self.debug.log(f"Called on_calc with keys: {inputs.keys()}")
        if inputs.changed("input_1"):
            self.input_values[0] = inputs.value("input_1")
        if inputs.changed("input_2"):
            self.input_values[1] = inputs.value("input_2")

    def on_timer(self, timer):
        pass

    def get_input_value(self, input_index):
        if input_index == 1 or input_index == 2:
            return self.input_values[input_index-1]
        else:
            return 0
