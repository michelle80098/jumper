import random

class Words:
    """
    Both the list of random words that are drawn from for the game as well as
    the selected word for the game instance. 

    Compares the guess from the player to the selected word. 

    Attributes:
        previous_guesses
        the_word
        correct_guesses
    """

    def __init__(self):
        """
        Constructs a new Words

        Args: self (Words): An instance of Words.
        """

        self._previous_guesses = []
        self._the_word = []
        self._correct_guesses = []
    
    def _create_words(self):
        """
        Creates a list of words
        """
        words = ['clark', 'michelle', 'dillon', 'grant', 'matt', 'object', 'oriented', 'programming', 'classes']

        return words


    def word_select(self):
        """
        Chooses a random word from the list of words created when 
        _create_words is called. Puts chosen word into a list where each 
        letter becomes an item in a list which is returned. 
        """
        words = self._create_words()
        the_word = random.choice(words)
        the_word.lower()

        print(the_word)

        #turn word into a list of letters
        letter = ''
        for letter in the_word:
            self._the_word.append(letter)

        return self._the_word
    


    def compare_words(self, guess):
        """
        Compares the parameter 'guess' to the _the_word and returns a boolean
        if the word contains the letter guess
        """
        if guess.lower() in self._the_word:
            is_correct = True
        else:
            is_correct = False
    
        return is_correct