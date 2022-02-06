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
        self.word = self.words.random

