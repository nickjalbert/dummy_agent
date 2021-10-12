import agentos


class DummyEnvironment(agentos.Environment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('Inside of DummyEnvironment.__init__()')
