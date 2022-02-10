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
        self._words = Word()
        self._jumper = Jumper()
        self._play = True
        


    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_guessing:
            self._get_inputs()
            # self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        tries = 5
        self._words.new_word()
        hidden_word = self._words.hide_word()
        print(hidden_word)
        self._parachute.show_parachute(tries=tries)
        tries -= 1 
        guess_letter = input("Guess a letter [a-z]: ")
        return guess_letter

    # def _do_updates(self, guess):
    #     pass

    def _do_outputs(self):
        self._is_guessing = False

    def play(self, word):
        self._parachute = Parachute()
        self._words = Word()
        self._is_guessing = False
        #play the game
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print((tries)) #not sure if it needs the display stages
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
            else:
                print("Not a valid guess.")
            print((tries))
            print(word_completion)
            print("\n")
        if self._is_guessing:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + self._words + ". Maybe next time!")
​ 
