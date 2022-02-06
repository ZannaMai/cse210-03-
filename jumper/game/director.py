from game.jumper import Jumper
from game.jumper import Parachute
from game.jumper import Word

class Director:


    """A person who directs the game

    Attributes:
        jumper:
        is_guessing: the player is guessing a letter
        player_correct: if the player is correct, that letter in the 
        puzzle is revealed
        player_incorrect: if the player is incorrect, a line is cut on the
        player's parachute
        puzzle_solved: if the puzzle is solved, the game is over
        no_parachute: if the player has no more parachute, the game is over
        
    """
    def __init__(self):
        """Constructs a new Director
        Args: 
            self(Director): an instance of Director.
        """
        self.jumper 
        self.parachute
        self.word
