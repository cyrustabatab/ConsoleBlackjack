

class Player:


    def __init__(self):
        self.cards = []
        self.possible_sums = {0}

    def add_card(self,card):

        for possible_sum in list(self.possible_sums):
            self.possible_sums.remove(possible_sum)
            for true_value in card.true_values:
                s = possible_sum + true_value
                self.possible_sums.add(s)



        self.cards.append(card)

    
    def reset(self):

        self.cards.clear()
        self.possible_sums = {0}

    @property
    def total(self):
        return max(self.possible_sums)
    
    
    @property
    def bust(self): 
        return not any(value < 21 for value in self.possible_sums)


    @property
    def has_natural(self):

        return 21 in self.possible_sums


    def __str__(self):
        return ','.join(str(card) for card in self.cards)  + '\nPossible Totals: ' + ','.join(map(str,sorted(self.possible_sums)))

class Dealer(Player):
    
    def flip_face_down_card(self):

        self.cards[1].flip()


    def __str__(self):
        return ','.join(str(card) for card in self.cards)



