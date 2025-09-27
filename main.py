import random


class Card:
    def __init__(self, color: str, number: str) -> None:
        self.color = color
        self.number = number

    def __str__(self) -> str:
        color = self.color
        number = self.number

        if self.number == "Discard":
            number = "Discard Card"

        return f"{color} {number}"


def display_all_cards(cards: list[Card], print_: bool = True) -> str:
    printed_str = ""

    for card in cards:
        printed_str += str(card) + ", "

    printed_str = printed_str[:-2]

    if print_:
        print(printed_str)

    return printed_str


def get_random_card():
    return Card(random.choice(CARD_COLORS), random.choice(CARD_NUMBERS))


CARD_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
CARD_COLORS = ["Red", "Blue", "Green", "Yellow"]

player_deck = [get_random_card() for _ in range(7)]
opponent_deck = [get_random_card() for _ in range(7)]
discard_pile = [Card(random.choice(CARD_COLORS), random.choice(CARD_NUMBERS))]

while True:
    cmd = input("What do you want to do? (view - view your cards)")

    match cmd:
        case "view":
            print("Your Cards:")
            display_all_cards(player_deck)
