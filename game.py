from deck import Deck
from player import Player,Dealer




class Blackjack:
    

    ace_values = {1,11}

    def __init__(self,num_decks=4,num_players=1,initial_amount=50):
        self.num_decks = num_decks
        self.deck = Deck(num_decks)
        
        self.player = Player(initial_amount)


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





        


    
    def _players_turn(self,bet):


        choice = self._get_stand_or_hit()


        while choice != 's':
            card = self.deck.remove_card()
            self.player.add_card(card)
            print(f"You are dealt {str(card)}")
            self._display_cards()
            if self.player.bust:
                self.player.money -= bet
                self.dealer.money += bet
                self.losses += 1
                print(f"You busted with a total of {self.player.bust_total}:( Dealer wins\n")
                return True

            
            choice = self._get_stand_or_hit()

        print()
        return False





    def _check_for_naturals(self):

        
        player_has_natural = self.player.has_natural
        

        dealer_has_natural = self.dealer.has_natural

        if player_has_natural and not dealer_has_natural:
            print("You have a natural blackjack! You win!")
            self.player.money += bet
            self.dealer.money -= bet
            self.wins += 1
        elif dealer_has_natural and not player_has_natural:
            print("Dealer has natural blackjack!. You lose :(")
            self.losses += 1
        elif player_has_natural and dealer_has_natural:
            self.player.money -= bet
            self.dealer.money += bet
            print("Both you and the dealer have a natural blackjack. Tie game")
            self.draws += 1
        
        return player_has_natural or dealer_has_natural

    def _dealers_turn(self,bet):

        self.dealer.flip_face_down_card()
        print("Dealer flips second card over")
        print(f"Dealers Cards: {self.dealer}")
        while not self.dealer.bust and self.dealer.total < 16:
            card = self.deck.remove_card()
            self.dealer.add_card(card)
            print(f"Dealer drew {str(card)}")
            print(f"Dealers Cards: {self.dealer}")


        if self.dealer.bust:
            self.wins += 1
            self.player.money += bet
            self.dealer.money -= bet
            print(f"Dealer busted with a total of  {self.dealer.bust_total}! You win")
        else:
            dealer_total = self.dealer.total
            player_total = self.player.total

            if player_total == dealer_total:
                print(f"Tie game with totals of {dealer_total}")
                self.draws += 1
            elif player_total > dealer_total:
                self.player.money += bet
                self.dealer.money -= bet
                self.wins += 1
                print(f"You win with a total of {player_total} versus {dealer_total}")
            else:
                self.player.money -= bet
                self.dealer.money += bet
                self.losses += 1
                print(f"Dealer wins with a total of {dealer_total} versus {player_total}")

    
    def _get_yes_or_no(self):

        
        valid_choices = ('y','yes','no','n')
        choice = None
        while choice not in valid_choices:

            choice = input("Play Again? ")


            if choice not in valid_choices:
                print("Please type one of 'yes','y','no', or 'n'")
                continue

        



        return choice[0] == 'y'










    

    def _get_bet(self):


        while True:

            bet = input("How much money do you want to bet? ")

            try:
                bet = float(bet)
            except:
                print("Please type a NUMBER")
                continue
            
            
            if bet <= 0 or bet > self.player.money:
                print("Please enter a valid bet(nonnegative and less than or equal to the money you have")
                continue



            return float(bet)



    def _display_cards(self):
        
        print()
        print(f"Your Cards: {self.player}")
        print(f"Dealers Cards: {self.dealer}")
        print()

    def _play(self):

        play_again = True 
        while play_again:

            print(f"Your Money: {self.player.money}\nDealer's Money: {self.dealer.money}\n")
            bet = self._get_bet()
            self._deal()

            self._display_cards()

            game_over = self._check_for_naturals()

            if not game_over:

                lose = self._players_turn(bet)
                
                if not lose:
                    self._dealers_turn(bet)

            
            if self.player.money <= 0:
                print("You have no money left :( GAME OVER")
                break

            play_again = self._get_yes_or_no()
            if play_again:
                self.dealer.reset()
                self.player.reset()
                print(f"Wins: {self.wins}\nLosses: {self.losses}\nDraws: {self.draws}")



        print(f"Wins: {self.wins}\nLosses: {self.losses}\nDraws: {self.draws}")
        print(f"Your Money: {self.player.money}\nDealer's Money: {self.dealer.money}\n")
        print("Thank you for playing!")





if __name__ == "__main__":
    


    Blackjack()

