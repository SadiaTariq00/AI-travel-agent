def get_flights(destination: str) -> str:
    price_offset = len(destination) % 3 * 25
    flight1 = 500 + price_offset
    flight2 = 450 + price_offset
    flight3 = 350 + price_offset

    return (
        f"✈️ **Flight options to {destination.title()}**:\n\n"
        f"🔹 **Option 1**: Non-stop flight – **${flight1}** (Fastest & most convenient)\n"
        f"🔹 **Option 2**: One stop – **${flight2}** (Balanced for time & price)\n"
        f"🔹 **Option 3**: Budget airline – **${flight3}** (Carry-on only, most affordable)"
    )
