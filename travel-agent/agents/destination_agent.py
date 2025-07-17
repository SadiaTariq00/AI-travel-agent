import random

class DestinationAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key 

        self.destinations = {
            "adventure": [
                {
                    "destination": "Murree, Pakistan",
                    "reason": "Hill stations, chairlifts, and scenic hiking trails.",
                    "tip": "Try hiking to Patriata for amazing views!"
                },
                {
                    "destination": "Rishikesh, India",
                    "reason": "Popular for river rafting, bungee jumping, and yoga camps.",
                    "tip": "Don't miss river rafting in the Ganges!"
                },
                {
                    "destination": "Chiang Mai, Thailand",
                    "reason": "Great mix of trekking, ziplining, and elephant sanctuaries.",
                    "tip": "Take a jungle trek to see waterfalls."
                }
            ],
            "relaxation": [
                {
                    "destination": "Maldives",
                    "reason": "Crystal-clear water, overwater villas, and total peace.",
                    "tip": "Book a spa day on the beach for pure relaxation."
                },
                {
                    "destination": "Dubai, UAE",
                    "reason": "Luxury hotels, desert calm, and world-class shopping.",
                    "tip": "Try an evening desert safari with BBQ dinner."
                },
                {
                    "destination": "Baku, Azerbaijan",
                    "reason": "Casual seaside walks, modern spas, and rich culture.",
                    "tip": "Walk along the Caspian Sea promenade at sunset."
                }
            ],
            "culture": [
                {
                    "destination": "Lahore, Pakistan",
                    "reason": "Home to forts, food streets, and Mughal architecture.",
                    "tip": "Visit Badshahi Mosque and eat at Fort Road Food Street."
                },
                {
                    "destination": "Istanbul, Turkey",
                    "reason": "Historic mosques, bazaars, and Byzantine history.",
                    "tip": "Take a Bosphorus ferry to enjoy both Europe and Asia sides!"
                },
                {
                    "destination": "Kathmandu, Nepal",
                    "reason": "Temples, festivals, and Himalayan history.",
                    "tip": "Visit Durbar Square for a taste of local life."
                }
            ]
        }

        self.fallbacks = [
            {
                "destination": "Kuala Lumpur, Malaysia",
                "reason": "Skyscrapers, street food, and shopping malls.",
                "tip": "Try the local satay and visit Petronas Towers."
            },
            {
                "destination": "Tashkent, Uzbekistan",
                "reason": "A unique mix of Soviet and Islamic architecture.",
                "tip": "Visit Chorsu Bazaar for local spices and breads."
            },
            {
                "destination": "Colombo, Sri Lanka",
                "reason": "Coastal charm, temples, and easy-paced lifestyle.",
                "tip": "Walk along Galle Face Green at sunset."
            }
        ]

    def suggest_destination(self, interest: str) -> dict:
        interest = interest.lower().strip()
        suggestions = self.destinations.get(interest)

        if suggestions:
            choice = random.choice(suggestions)
        else:
            choice = random.choice(self.fallbacks)

        return {
            "destination": choice["destination"],
            "reason": choice["reason"],
            "tip": choice["tip"]
        }
