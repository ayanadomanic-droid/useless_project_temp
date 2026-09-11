import random

print("===================================")
print("       🌦️ USELESS WEATHER REPORT")
print("===================================")

# Get information from the user
city = input("Enter your city: ")

temperature = float(input("Enter temperature in °C: "))

condition = input("Enter weather condition: ").lower()

humidity = int(input("Enter humidity (%): "))


print("\nGenerating completely useless information...")
print()


# -----------------------------------
# DRAMA LEVEL
# -----------------------------------

if temperature > 35:
    drama = random.randint(85, 100)

elif temperature > 30:
    drama = random.randint(65, 85)

elif temperature < 20:
    drama = random.randint(40, 70)

else:
    drama = random.randint(20, 60)


# -----------------------------------
# MOTIVATION LEVEL
# -----------------------------------

if "rain" in condition:
    motivation = random.randint(1, 20)

elif "storm" in condition:
    motivation = random.randint(1, 10)

else:
    motivation = random.randint(20, 70)


# -----------------------------------
# FROG ACTIVITY
# -----------------------------------

if "rain" in condition:
    frog = "EXTREMELY HIGH 🐸"

elif "cloud" in condition:
    frog = "Probably plotting 🐸"

else:
    frog = "Taking a day off 🐸"


# -----------------------------------
# BRAIN FUNCTION
# -----------------------------------

brain_messages = [
    "12% - Please wait...",
    "37% - Functioning somehow",
    "4% - Thinking about food",
    "68% - Surprisingly operational",
    "1% - Completely offline",
    "52% - Loading..."
]

brain = random.choice(brain_messages)


# -----------------------------------
# OUTFIT
# -----------------------------------

outfits = [
    "Sunglasses + formal shirt + confidence 😎",
    "Umbrella + jeans + unnecessary optimism ☂️",
    "Black outfit + mysterious personality 🖤",
    "Anything comfortable. Nobody is judging.",
    "Traditional outfit + absolutely no explanation.",
    "Blazer + slippers. Trust the process."
]

outfit = random.choice(outfits)


# -----------------------------------
# WEATHER PERSONALITY
# -----------------------------------

personalities = [
    "The dramatic one in the group.",
    "That friend who always cancels plans.",
    "Quiet but suspicious.",
    "Main character for absolutely no reason.",
    "Woke up and chose chaos.",
    "Emotionally unavailable cloud.",
    "Has no idea what is happening."
]

personality = random.choice(personalities)


# -----------------------------------
# SHOULD I GO OUTSIDE?
# -----------------------------------

outside_answers = [
    "NO. The universe said stay home. 🛌",
    "Absolutely not. Try again tomorrow.",
    "Maybe... but why risk it?",
    "YES. Go outside and touch some grass. 🌱",
    "NO. You have officially been excused from society.",
    "YES. Something interesting might happen.",
    "Stay inside. This is probably a sign."
]

outside = random.choice(outside_answers)


# -----------------------------------
# FINAL REPORT
# -----------------------------------

print("===================================")
print("          🌦️ WEATHER REPORT")
print("===================================")

print("📍 City:", city)
print("🌡️ Temperature:", temperature, "°C")
print("☁️ Condition:", condition)
print("💧 Humidity:", humidity, "%")

print()
print("🤡 COMPLETELY USELESS ANALYSIS")
print("-----------------------------------")

print("🎭 Drama Level:", drama, "%")

print("😴 Motivation:", motivation, "%")

print("🐸 Frog Activity:", frog)

print("🧠 Brain Function:", brain)

print("👕 Recommended Outfit:", outfit)

print("🌤️ Weather Personality:", personality)

print()
print("🚪 SHOULD I GO OUTSIDE?")
print(outside)

print()
print("===================================")
print("Thank you for using a completely")
print("unnecessary weather application.")
print("===================================")