import random


class Deck(object):
    def __init__(self, draw, hand, discard):
    def draw(until):
        next_cards = gen_next_cards()
        while len(hand) < until:            
            self.hand.add(next(next_cards))
    def discard_hand():
        

    def gen_next_cards():
        while True:
            if len(self.draw) == 0:
                random.shuffle(self.discard)
                self.draw = self.discard
                self.discard = []

            next_card = self.draw.pop()
            yield next_card
