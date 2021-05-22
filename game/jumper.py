
class Jumper:
    """The jumper class holds and manages the board that 
        shows when you missed a letter.
    
    Stereotype:
        Board

    Attributes:
        jumper (Jumper) An instance of the class of objects known as Jumper.
    """

    def __init__(self) :
        """The class constructor.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.parachute = "\n  ___ \n /___\ \n \   /  \n  \ / \n   0 \n  /|\ \n  / \ \n"



    def get_board(self):
        """The board creator.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        return self.parachute

    def remove_pieces(self,guess_val):
        """The board updater.
        
        Args:
            self (Jumper): an instance of Jumper.
            guess_val: a variable that counts downs till 0 which triggers updates of the parachute guy
        """
        if guess_val == 3:
            self.parachute = self.parachute.replace("  ___ \n", "")
        elif guess_val == 2:
            self.parachute = self.parachute.replace(" /___\ \n", "")
        elif guess_val == 1:
            self.parachute = self.parachute.replace(" \   /  \n", "")
        elif guess_val == 0:
            self.parachute = self.parachute.replace("  \ / \n", "")
            self.parachute = self.parachute.replace("0", "X")
