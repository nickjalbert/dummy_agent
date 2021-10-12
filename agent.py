import agentos


class DummyAgent(agentos.Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('Inside of DummyAgent.__init__()')

    def evaluate(self, num_episodes):
        print("Inside of DummyAgent.evaluate()")

    def learn(self, num_episodes):
        print("Inside of DummyAgent.learn()")
