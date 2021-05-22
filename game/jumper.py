
class Jumper:

    def __init__(self) :
        parachute = ["  ___ "," /___\ ", " \   /  ", "  \ / ","   0 ","  /|\ ", "  / \ "]



    def get_board(self):

        for i in range(0, len(self.parachute)):
            print(f"{self.parachute[i]}")

            #return self.parachute

    def remove_pieces(self,guess_val):
        if guess_val == 3:
            self.parachute.remove("  ___ ")
        elif guess_val == 2:
            self.parachute.remove(" /___\ ")
        elif guess_val == 1:
            self.parachute.remove(" \   /  ")
        elif guess_val == 0:
            self.parachute.remove("  \ / ")
