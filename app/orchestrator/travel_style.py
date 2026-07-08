from app.agents.travel_style_agent import TravelStyleAgent


agent = TravelStyleAgent()


def process_travel_style(style):

    return agent.run(style)