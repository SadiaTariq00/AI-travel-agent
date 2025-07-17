import chainlit as cl
import os
from dotenv import load_dotenv
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent


load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise ValueError("GEMINI_API_KEY is not set. Please make sure it’s defined in your .env file.")

destination_agent = DestinationAgent(gemini_key)
booking_agent = BookingAgent(gemini_key)
explore_agent = ExploreAgent()


state = {"stage": "start", "destination": ""}

@cl.on_chat_start
async def start():
    state["stage"] = "destination"
    await cl.Message(
        content=(
            "🌟 **Welcome to TravelBuddy — your intelligent trip planner!**\n\n"
            "I’m here to help you design an incredible getaway — from picking the destination to flights, hotels, food, and local highlights.\n\n"
            "**Tell me what kind of vibe you're looking for:**\n"
            "🔹 `Adventure` – wild hikes, rafting, thrill rides\n"
            "🔹 `Relaxation` – beaches, nature, wellness\n"
            "🔹 `Culture` – history, landmarks, local experiences\n\n"
            "📬 *Type your preferred theme to begin!*"
        )
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = message.content.lower().strip()

    if state["stage"] == "destination":
        suggestion = destination_agent.suggest_destination(msg)
        if suggestion:
            state["destination"] = suggestion["destination"]
            state["stage"] = "booking"
            await cl.Message(
                content=(
                    f"📌 **Your Ideal Destination:** `{suggestion['destination']}`\n"
                    f"🧠 *Reason*: {suggestion['reason']}\n\n"
                    "🛫 Would you like to see available flights and hotel suggestions now?"
                )
            ).send()
        else:
            await cl.Message(
                content=(
                    "🤔 I didn’t catch that travel style.\n"
                    "Try one of these options instead: `adventure`, `relaxation`, or `culture`."
                )
            ).send()

    elif state["stage"] == "booking":
        destination = state["destination"]
        flights = booking_agent.get_flights(destination)
        hotels = booking_agent.suggest_hotels(destination)
        state["stage"] = "explore"
        await cl.Message(
            content=(
                f"🛫 **Flights to {destination.title()}**\n{flights}\n\n"
                f"🛏️ **Hotel Suggestions**\n{hotels}\n\n"
                "📍 Ready to explore the top things to do there?"
            )
        ).send()

    elif state["stage"] == "explore":
        destination = state["destination"]
        guide = explore_agent.explore(destination)
        state["stage"] = "done"
        await cl.Message(
            content=(
                f"🌍 **Discover {destination.title()}**\n{guide}\n\n"
                "✅ That’s your full travel plan!\n"
                "Want to plan another trip? Just type anything to get started again."
            )
        ).send()

    else:
        state["stage"] = "destination"
        await cl.Message(
            content=(
                "🔄 Let’s plan something new!\n"
                "What type of experience are you in the mood for?"
            )
        ).send()
