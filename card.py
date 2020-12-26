




class Card:
    
    


    






    def __init__(self,rank,suit,face_up=True):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up


    def flip(self):
        self.face_up = not self.face_up

    def set_face_down(self):
        self.face_up = False
    

    @property
    def true_values(self):

        if self.rank in range(2,11):
            return (self.rank,)
        elif self.rank == 'ACE':
            return (1,11)
        else:
            return (10,)

    def __str__(self):
        return f"{self.rank} of {self.suit}'s" if self.face_up else 'FACE DOWN CARD'
    

    def __repr__(self):
        return f"Card({self.rank},{self.suit})"
