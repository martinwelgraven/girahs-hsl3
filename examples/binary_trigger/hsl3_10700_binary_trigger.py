class LogicModule:
    def __init__(self, hsl3):
        self.fw = hsl3
        self.debug = self.fw.create_debug_section()

    def on_init(self, inputs, store):
        self.debug.log(f"Called on_init with keys: {inputs.keys()}")

    def on_calc(self, inputs):
        self.debug.log(f"Called on_calc with keys: {inputs.keys()}")
        input_value = inputs.value("input")
        output_1 = float(input_value!=0)
        output_2 = float(input_value==0)
        self.fw.set_output("not_equal_to_zero", output_1)
        self.fw.set_output("equal_to_zero", output_2)

    def on_timer(self, timer):
        pass