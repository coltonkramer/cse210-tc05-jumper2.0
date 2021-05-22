import random

class Word:

    def __init__(self):
        self.word = "hello"
        self.list_word = []
        self.show_guess = ""
        self.wrong_guesses = 4

    def update_word(self):
        """This class chooses a word for the game and then makes the the tiles."""
        val = random.randint(1,3)
        if val == 1:
            self.word = "chicken"
        elif val == 2:
            self.word = "flag"
        elif val == 3:
            self.word = "pikachu"

        #use the code below to also update when the player chooses a correct guess
        for x in range(0, len(self.word)):
            self.list_word.append("_ ")
            self.show_guess = self.show_guess + self.list_word[x]
        

    def guessed_letter(self, letter):
        """This function looks through each of the letters for the user's inputted letter to check if it needs to replace any of the letters in the displayed word"""
        wrong = 0
        self.show_guess = ""

        for x in range(0, len(self.word)):
            if letter == self.word[x]:
                self.list_word[x] = letter
                self.show_guess = self.show_guess + self.list_word[x]
            else:
                wrong += 1
                self.show_guess = self.show_guess + self.list_word[x]

        if(wrong == len(self.word)):
            self.wrong_guesses = self.wrong_guesses -1


    def keep_playing(self):
        
        if(self.wrong_guesses == 0):
            return(False)
        elif(self.word == self.show_guess):
            return(False)
        else:
            return(True)