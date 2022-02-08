import random
class Word:

    def __init__(self):
        """Constructs a new Word 

        Args: 
            self(Word): a new instance of Word
        """
        #self._words is encapsulated so that it is protected within this method
        self._words = []
        self.word = ''


    def new_word(self):
        self.word = random.choice(self._words)


    def hide_word(self):
        letters = Word.new_word(self)
        for i in range(len(letters)):
            letters[i] = "_"
        letters = ', '.join(letters)
        letters = ''.join(str(letters).split(','))
        return letters


    def check_guess():
        pass 