from game.jumper import Jumper
from game.parachute import Parachute
from game.word import Word

class Director:


    """A person who directs the game
    Attributes:
        jumper (Jumper): the game's jumper
        is_guessing (boolean): whether or not to keep playing
        parachute (Parachute): Player's parachute
        jumper (Jumper): For getting and displaying information on the terminal        
    """
    def __init__(self):
        """Constructs a new Director
        Args: 
            self(Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._is_guessing = True
        self._word = Word()
        self._jumper = Jumper()
        self.guessed_word = ""
        self.tries = 5
        self.hidden_word = []
        


    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self.guessed_word = self._word.new_word()
        self.hidden_word = self._word.letters
        self._word.print_blanks()
        self._parachute.show_parachute(self.tries)
        while self._is_guessing:
            guess = self._get_inputs()
            self._do_updates(guess)
            self._do_outputs()

    def _get_inputs(self):
        guess_letter = input("Guess a letter [a-z]: ")
        return guess_letter

    def _do_updates(self, guess):
        wrong_letter = []
        found_letter = False
        chosen_word = []

        for letter in self.guessed_word:
            chosen_word.append(letter)

        for i in range(0, len(chosen_word)):
            letter = chosen_word[i]
            if guess == letter:
                self._word.letters[i] = letter
                found_letter = True
                print("Yay! You guessed a correct letter :)")

        if found_letter == False:
            self.tries -= 1
            print("Sorry! This letter was not correct. Please try again :)")
            wrong_letter.append(guess)
            print(wrong_letter)

        self._word.print_blanks()
        self._parachute.show_parachute(self.tries)
            

    def _do_outputs(self):
        # when all the parachute strings ae gone..
        # when all the blanks are filled...
        if self.tries == 0:
            self._is_guessing = False
            print("Sorry you lost")
        
        # see if there any underscores left in the list 
        if "_" not in self._word.letters:
            self._is_guessing = False
            print("Congrats! You win!")
