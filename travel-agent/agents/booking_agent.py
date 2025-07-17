from tools.flights import get_flights
from tools.hotels import suggest_hotels


class BookingAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key  # Reserved for future integration (e.g. external APIs)

    def get_flights(self, destination: str) -> str:
        # Uses the flights tool function
        return get_flights(destination)

    def suggest_hotels(self, destination: str) -> str:
        # Uses the hotels tool function
        return suggest_hotels(destination)
