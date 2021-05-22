from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        #The two line below make it so the player see's what they are originally working with.
        self.word.update_word()
        self.do_outputs()

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means setting up the board.

        Args:
            self (Director): An instance of Director.
        """
        #self.console.write(self.word.show_guess)
        #board = self.jumper.get_board()
        #self.console.write(board)
        letter = self.console.read("Guess a letter [a-z]: ")
        self.word.guessed_letter(letter)
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        self.jumper.remove_pieces(self.word.wrong_guesses)
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.word.show_guess)
        board = self.jumper.get_board()
        self.console.write(board)
        self.keep_playing = (self.word.keep_playing())