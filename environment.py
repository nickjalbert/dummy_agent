import agentos


class DummyEnvironment(agentos.Environment):
    def init(self, **kwargs):
        print('Running DummyEnvironment.init()')
