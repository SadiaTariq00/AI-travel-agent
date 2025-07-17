class ExploreAgent:
    def explore(self, destination: str) -> str:
        destination = destination.lower().strip()

        guides = {
            "murree, pakistan": (
                "- 🏞️ **Patriata Chairlift** – Ride above forests with mountain views\n"
                "- ❄️ **Mall Road Stroll** – Enjoy local snacks, jackets & cold breeze\n"
                "- ☕ **Coffee with a View** – Try cafes with hilltop seating\n"
                "- 🥾 **Kashmir Point Walk** – A peaceful walk with pine-covered paths"
            ),
            "rishikesh, india": (
                "- 🌊 **River Rafting** – Thrilling ride on the Ganges\n"
                "- 🧘 **Morning Yoga** – Join open-air sessions by the river\n"
                "- 🌉 **Laxman Jhula Visit** – Iconic suspension bridge experience\n"
                "- 🕉️ **Evening Ganga Aarti** – Peaceful prayers with lamps & chanting"
            ),
            "phuket, thailand": (
                "- 🏖️ **Kata Beach** – Swim or relax with a coconut drink\n"
                "- 🛕 **Wat Chalong Temple** – Explore beautiful Thai architecture\n"
                "- 🚤 **Island Tour** – Visit Phi Phi or James Bond Island by boat\n"
                "- 🍢 **Night Market Food** – Try spring rolls, mango sticky rice, and more"
            ),
            "lahore, pakistan": (
                "- 🕌 **Badshahi Mosque** – Mughal-era marvel with peaceful courtyard\n"
                "- 🍲 **Food Street** – Taste biryani, BBQ, and jalebi with a fort view\n"
                "- 🏰 **Lahore Fort Tour** – Discover centuries of history and art\n"
                "- 🧵 **Anarkali Bazaar** – Shop for clothes, crafts, and local gifts"
            ),
            "istanbul, turkey": (
                "- 🕌 **Blue Mosque Visit** – Majestic domes and peaceful silence\n"
                "- 🚢 **Bosphorus Ferry Ride** – Sail between Europe & Asia\n"
                "- 🛍️ **Grand Bazaar** – Shop spices, lamps, and souvenirs\n"
                "- ☕ **Turkish Tea & Baklava** – Enjoy a sweet break at a local café"
            )
        }

        return guides.get(
            destination,
            "📍 I don’t have a guide for this place yet.\nTry Google Maps or TripAdvisor once you're there! 🌐"
        )
