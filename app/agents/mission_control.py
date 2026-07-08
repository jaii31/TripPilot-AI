from app.agents.destination_agent import DestinationAgent


class MissionControl:

    def __init__(self):

        self.state = {}

        self.destination_agent = DestinationAgent()

    def update(self, key, value):

        self.state[key] = value

    def get(self, key):

        return self.state.get(key)

    def execute_destination_agent(self):

        result = self.destination_agent.execute(self)

        self.state.update(result)

        return result

    def summary(self):

        return self.state