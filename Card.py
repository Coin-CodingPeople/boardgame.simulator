"""
Created by hangeonho on 2018. 10. 1..
"""

card_category = ("function", "operator", "number", "magic", "execute")


class Card:
    def __init__(self, category, value):
        self.category = category
        self.value = value


class FunctionCard(Card):
    pass


class OperatorCard(Card):
    pass


class NumberCard(Card):
    pass


class MagicCard(Card):
    pass


class ExecuteCard(Card):
    pass
