from app.agents.destination_agent import DestinationAgent
from app.agents.explorer import ExplorerAgent
from app.agents.strategist import Strategist
from app.agents.budget_agent import BudgetAgent


class MissionControl:

    def __init__(self):

        self.state = {}

        self.destination_agent = DestinationAgent()

        self.explorer_agent = ExplorerAgent()

        self.strategist = Strategist()

        self.budget_agent = BudgetAgent()

    def update(self, key, value):

        self.state[key] = value

    def get(self, key):

        return self.state.get(key)

    def summary(self):

        return self.state

    def trip_length(self):

        dates = self.get("dates")

        if (
            isinstance(dates, (tuple, list))
            and len(dates) == 2
        ):

            start, end = dates

            return (
                end - start
            ).days + 1

        return 1

    def execute_destination_agent(self):

        result = (
            self.destination_agent
            .execute(self)
        )

        self.state.update(result)

        return result

    def execute_explorer_agent(self):

        result = (
            self.explorer_agent
            .execute(self)
        )

        self.state.update(result)

        return result

    def execute_strategist_agent(self):

        result = (
            self.strategist
            .execute(self)
        )

        self.state.update(result)

        return result

    def execute_budget_agent(self):

        result = (
            self.budget_agent
            .execute(self)
        )

        self.state.update(result)

        return result