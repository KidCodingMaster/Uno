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
