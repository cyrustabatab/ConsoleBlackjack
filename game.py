from deck import Deck
from player import Player,Dealer




class Blackjack:
    

    ace_values = {1,11}

    def __init__(self,num_decks=4,num_players=1):
        self.num_decks = num_decks
        self.deck = Deck(num_decks)
        
        self.player = Player()


        self.dealer = Dealer()

        self.wins = self.losses = self.draws = 0

        self._play()

    

    def _shuffle(self):
        # add cut here possibly

        self.deck.shuffle()

    def _deal(self):
    

        for i in range(2):
            card = self.deck.remove_card()
            self.player.add_card(card)
            print(f"You are dealt {str(card)}")

            card = self.deck.remove_card(False if i == 1 else True)
            
            self.dealer.add_card(card)
            if i == 0:
                print(f"Dealer drew {str(card)}")
        
            
        print()

    def _get_stand_or_hit(self):
        
        valid_choices = {'s','h','stand','hit'}

        while True:

            choice = input("Stand or Hit? ").lower()

            if choice not in valid_choices:
                print("Please type one of 's','h','stand',or 'hit'")
                continue


            return choice[0]





        


    
    def _players_turn(self):


        choice = self._get_stand_or_hit()


        while choice != 's':
            card = self.deck.remove_card()
            self.player.add_card(card)
            print(f"You are dealt {str(card)}")
            self._display_cards()
            if self.player.bust:
                print("You busted :( Dealer wins\n")
                return True

            
            choice = self._get_stand_or_hit()

        print()
        return False





    def _check_for_naturals(self):

        
        player_has_natural = self.player.has_natural
        

        dealer_has_natural = self.dealer.has_natural

        if player_has_natural and not dealer_has_natural:
            print("You have a natural blacjack! You win!")
        elif dealer_has_natural and not player_has_natural:
            print("Dealer has natural blackjack!. You lose :(")
        elif player_has_natural and dealer_has_natural:
            print("Both you and the dealer have a natural blackjack. Tie game")
        
        return player_has_natural or dealer_has_natural
    def _dealers_turn(self):

        self.dealer.flip_face_down_card()
        print("Dealer flips second card over")
        print(f"Dealers Cards: {self.dealer}")
        while not self.dealer.bust and self.dealer.total < 16:
            card = self.deck.remove_card()
            self.dealer.add_card(card)
            print(f"Dealer drew {str(card)}")
            print(f"Dealers Cards: {self.dealer}")


        if self.dealer.bust:
            print("Dealer busted! You win")
        else:
            dealer_total = self.dealer.total
            player_total = self.player.total

            if player_total == dealer_total:
                print(f"Tie game with totals of {dealer_total}")
            elif player_total > dealer_total:
                print(f"You win with a total of {player_total}")
            else:
                print(f"Dealer wins with a total of {dealer_total}")



    def _display_cards(self):

        print(f"Your Cards: {self.player}")
        print(f"Dealers Cards: {self.dealer}")
        print()

    def _play(self):


        self._deal()

        self._display_cards()

        game_over = self._check_for_naturals()

        if not game_over:

            lose = self._players_turn()
            
            if not lose:
                self._dealers_turn()






if __name__ == "__main__":
    


    Blackjack()

