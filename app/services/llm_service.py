import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:

            raise ValueError(
                "Gemini API key is unavailable."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_response(
        self,
        user_message,
        mission=None,
        chat_history=None
    ):

        trip_data = (
            mission.summary()
            if mission
            else {}
        )

        trip_context = json.dumps(
            trip_data,
            default=str,
            indent=2
        )

        recent_history = (
            chat_history[-6:]
            if chat_history
            else []
        )

        conversation = "\n".join(

            f"{message['role']}: "
            f"{message['content']}"

            for message
            in recent_history
        )

        prompt = f"""
You are TripPilot AI Copilot, an intelligent
multi-agent travel planning assistant.

CURRENT JOURNEY DATA:
{trip_context}

RECENT CONVERSATION:
{conversation}

CURRENT USER QUESTION:
{user_message}

RESPONSE RULES:

1. Use the traveller's actual journey data.

2. Respect the selected destination, route,
dates, travel style, number of travellers
and budget.

3. Give practical and actionable advice.

4. Explain important recommendations briefly.

5. Never claim that estimated information is
live, booked or guaranteed.

6. Never invent current ticket availability,
hotel availability, live prices or exact
weather.

7. Clearly distinguish estimates from live data.

8. Do not unnecessarily change the traveller's
original plan.

9. Use short headings and bullet points when
useful.

10. Keep the response concise unless the
traveller requests detail.
"""

        response = (
            self.client.models
            .generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
        )

        if not response.text:

            return (
                "I could not generate a useful "
                "travel recommendation. Please "
                "try rephrasing your question."
            )

        return response.text