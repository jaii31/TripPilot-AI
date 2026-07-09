from app.agents.destination_agent import DestinationAgent
from app.agents.explorer import ExplorerAgent
from app.agents.strategist import Strategist
from app.agents.budget_agent import BudgetAgent
from app.agents.transport_agent import TransportAgent
from app.agents.accommodation_agent import AccommodationAgent
from app.agents.activity_agent import ActivityAgent
from app.agents.forecaster import Forecaster
from app.agents.packwise import Packwise

class MissionControl:

    def __init__(self):

        self.state = {}

        self.destination_agent = DestinationAgent()

        self.explorer_agent = ExplorerAgent()

        self.strategist = Strategist()

        self.budget_agent = BudgetAgent()

        self.transport_agent = TransportAgent()

        self.accommodation_agent = AccommodationAgent()

        self.activity_agent = ActivityAgent()

        self.forecaster = Forecaster()

        self.packwise = Packwise()

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
    
    def execute_transport_agent(self):

        result = (
            self.transport_agent
            .execute(self)
        )

        self.state.update(result)

        return result
    
    def execute_accommodation_agent(self):

        result = self.accommodation_agent.execute(self)

        self.state.update(result)

        return result
    
    def execute_activity_agent(self):

        result = self.activity_agent.execute(self)

        self.state.update(result)

        return result
    
    def execute_forecaster(self):

        result = self.forecaster.execute(self)

        self.state.update(result)

        return result
    
    def execute_packwise(self):

        result = self.packwise.execute(self)

        self.state.update(result)

        return result