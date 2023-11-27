class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, _):
        if len(self.inputs) > 0:
            try:
                return self.inputs.pop(0)
            except:
                import traceback
                print(traceback.format_exc())
        return ""

    def add_input(self, value):
        self.inputs.append(value)
