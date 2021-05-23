import random
import csv

class Word:
    """Controls the mechanics of the word in the game. Chooses the word, checks 
       if the guess is correct, and checks if you can keep playing.
    
    Stereotype:
        Game logic

    Attributes:
        word (Word): An instance of the class of objects known as Word.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): an instance of Word.
        """

        self.word = "hello"
        self.list_word = []
        self.show_guess = ""
        self.wrong_guesses = 4
        self.list = []

    def update_word(self):
        """This class chooses a word for the game and then makes the the tiles."""
        val = random.randint(1,10000)

        with open('Words.csv') as words:
        
            for i in words:
                i = i.strip()
                # self.word = i.split(',')
                self.list.append(i)
            
            self.word = self.list[val]


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
        """ This function checks to see if the player can contine the game"""
        if(self.wrong_guesses == 0):
            print('The correct answer is: '+ self.word.capitalize())
            return(False)
        elif(self.word == self.show_guess):
            return(False)
        else:
            return(True)