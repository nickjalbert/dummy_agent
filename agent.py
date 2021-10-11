import agentos


class DummyAgent(agentos.Agent):
    def init(self, **kwargs):
        print('Running DummyAgent.init()')

    def evaluate(self, num_episodes):
        print("Running DummyAgent.evaluate()")

    def learn(self, num_episodes):
        print("Running DummyAgent.learn()")
