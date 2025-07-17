# 🧳 AI Travel Designer (Gemini + Chainlit)

Plan your perfect trip with AI — from destination suggestions to flights, hotels, and activities — all in one interactive assistant powered by Google Gemini and Chainlit.

---

## ✨ Features

- 🌍 **Smart Destination Suggestions**  
  Choose from travel moods like `adventure`, `relaxation`, or `culture`, and get personalized travel recommendations.

- ✈️ **Flight & Hotel Listings**  
  Displays example flights and hotels with clean formatting and emoji-enhanced presentation.

- 🗺️ **Explore Local Experiences**  
  Discover handpicked activities, food, and sightseeing options in your selected destination.

- 🧠 **Powered by Google Gemini API**  
  Using Chainlit’s framework and modular agents to guide your travel flow.

---

## 📁 Project Structure

travel-agent/
├── main.py                  # Main chat logic (Chainlit app entry point)
├── .env                     # Stores GEMINI_API_KEY
│
├── agents/
│   ├── destination_agent.py # Suggests destinations based on mood
│   ├── booking_agent.py     # Handles flights & hotels
│   └── explore_agent.py     # Lists local activities
│
├── tools/
│   ├── flights.py           # flight logic
│   └── hotels.py            # hotel logic
│



## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/ai-travel-designer.git
   cd ai-travel-designer

   Create a virtual environment

2. setup virtual environment  
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Create a .env file:
GEMINI_API_KEY=your_google_gemini_api_key

4.Run the app
chainlit run main.py
