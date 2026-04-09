import random

subjects = [
    "Fawad Khan",
    "Bilal Ashraf",
    "Shahid Afridi",
    "Islamabad",
    "Lahorites",
    "Imran Khan",
    "Birds"
]

actions = [
    "launches",
    "cancels",
    "eats",
    "dances with",
    "orders",
    "celebrates",
]

places_or_things = [
    "Bagh",
    "Inside Parliament",
    "During PSL match",
    "at Al Khan",
    "on Eid ul Fitr",
    "on Easter",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day!")