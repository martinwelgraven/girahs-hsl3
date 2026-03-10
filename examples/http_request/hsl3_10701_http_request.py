import threading
import requests

class LogicModule:
    def __init__(self, hsl3):
        self.fw = hsl3
        self.debug = self.fw.create_debug_section()
        self.param_in_value = ""
        self.param_out_value = ""

    def on_init(self, inputs, store):
        self.debug.log(f"Called on_init with keys: {inputs.keys()}")
        self.param_in_value =  inputs.value("param_in")

    def on_calc(self, inputs):
        self.debug.log(f"Called on_calc with keys: {inputs.keys()}")
        if inputs.changed("param_in"):
            self.param_in_value = inputs.value("param_in")
        if inputs.changed("trigger") and bool(inputs.value("trigger")):
            thread = threading.Thread(target=self.fetch_data)
            thread.start()

    def on_timer(self, timer):
        pass

    def fetch_data(self):
        url = "https://httpbin.org/get"
        params = {"foo": "bar", "my_test_param": self.param_in_value}
        self.debug.log(f"Get URL: {url}")
        response = requests.get(url, params=params)
        self.debug.log(f"Received response: {response.content[:60]}")
        self.param_out_value = response.json()["args"]["my_test_param"]
        self.fw.run_in_context(self.set_output, ())

    def set_output(self):
        self.fw.set_output("param_out", self.param_out_value.encode("iso-8859-15"))
