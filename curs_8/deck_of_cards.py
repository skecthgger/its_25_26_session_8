import random

# As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
deck_of_cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "As": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

print(deck_of_cards)

random.shuffle(deck_of_cards)

print(deck_of_cards)