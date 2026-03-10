class LogicModule:
    def __init__(self, hsl3):
        self.fw = hsl3
        self.debug = self.fw.create_debug_section()
        self.server_instance = None

    def on_init(self, inputs, store):
        self.debug.log(f"Called on_init with keys: {inputs.keys()}")
        self.fw.set_timer("timer_1_sec", 1)

    def on_calc(self, inputs):
        self.debug.log(f"Called on_calc with keys: {inputs.keys()}")
        instance_id_server = inputs.value("instance_id_server")
        self.server_instance = self.fw.get_instance(instance_id_server)

    def on_timer(self, timer):
        if timer.changed("timer_1_sec"):
            if self.server_instance!=None:
                server_input_value_1 = self.server_instance.get_input_value(1)
                server_input_value_2 = self.server_instance.get_input_value(2)
                self.fw.run_in_context(self.set_output_values, (server_input_value_1, server_input_value_2))
            self.fw.set_timer("timer_1_sec", 1)

    def set_output_values(self, output_value_1, output_value_2):
        self.fw.set_output("server_input_1", output_value_1)
        self.fw.set_output("server_input_2", output_value_2)
