
class Jumper:

    def __init__(self) :
        self.parachute = "\n  ___ \n /___\ \n \   /  \n  \ / \n   0 \n  /|\ \n  / \ \n"



    def get_board(self):

        """
        for i in range(0, len(self.parachute)):
            print(f"{self.parachute[i]}")
        """
        return self.parachute

    def remove_pieces(self,guess_val):
        if guess_val == 3:
            self.parachute = self.parachute.replace("  ___ \n", "")
        elif guess_val == 2:
            self.parachute = self.parachute.replace(" /___\ \n", "")
        elif guess_val == 1:
            self.parachute = self.parachute.replace(" \   /  \n", "")
        elif guess_val == 0:
            self.parachute = self.parachute.replace("  \ / \n", "")
            self.parachute = self.parachute.replace("0", "X")
