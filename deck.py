from card import Card
import random



class Deck:

    SUITS = ["HEART","SPADE","CLUB","DIAMONDS"]
    RANKS = list(range(2,11)) + ['JACK','QUEEN','KING','ACE']
    def __init__(self,decks=4):

        self._create_deck(decks)


    def _create_deck(self,decks):

        self.cards = [Card(rank,suit) for _ in range(decks) for rank in self.RANKS for suit in self.SUITS]
        self.shuffle()
    

    def remove_card(self,face_up=True):


        card = self.cards.pop()
        if not face_up:
            card.set_face_down()
        
        
        if self.empty:
            self._create_deck()

        return card


    @property
    def empty(self):
        return not self.cards


    
    def shuffle(self):

        random.shuffle(self.cards)

    def __repr__(self):


        return str(self.cards)












