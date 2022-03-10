from multiprocessing import log_to_stderr
from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.words import Words 

class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """
    def __init__(self):
        self._is_playing = True
        self.words = Words()
        self.jumper = Jumper()
        self.terminal_service = TerminalService()
        self.letter = None
        self.master_word = None
        self.drawing = None
        self.word_dashes = None
        self.lives = 4

        """ Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        

    def start_game(self):
        master_word = self.words.word_select()
        self.master_word = master_word
        drawing, word_dashes = self.jumper.create_drawing(self.master_word)
        self.terminal_service.draw_picture(drawing, word_dashes)

        # The Main Game Loop
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        # TODO TODO TODO
        # If endgame conditions are met the word, picture, and your guesses would be printed
        self.terminal_service.draw_picture(self.drawing, self.word_dashes)
        self.terminal_service.display_end_game(self.master_word, self.lives)


    def _get_inputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        #
        letter = self.terminal_service.read_text()
        self.letter = letter
        

    def _do_updates(self):
        # Compare the letter guessed to the word selected
        boolean = self.words.compare_words(self.letter)
        assert type(boolean) == bool
        
        # If not False (or true) Then they must have guessed incorrectly, thus they lose a life.
        if not boolean:
            self.lives -= 1

        # The guess is then sent to jumper so the drawing can be updated
        self.jumper.guess(boolean, self.letter)

        # The drawing created and the list of dashes (or correct words) are retrieved and then put in variables
        # to eventually be given to the terminal service for printing.
        drawing, word_dashes = self.jumper.update_drawing()
        self.drawing, self.word_dashes = drawing, word_dashes

        """
        Args:
            self (Director): An instance of Director.
        """


    def _do_outputs(self):
        # The picture is drawn and printed to terminal
        self.terminal_service.draw_picture(self.drawing, self.word_dashes)

        # Lives are calculated to check if an end condition is met for the sentinel loop.
        if self.lives == 0:
            self._is_playing = False
        
        # The guesses are calculated to see if all the letters within the word have been guessed.
        have_won = self.jumper.winner()
        if have_won:
            self._is_playing = False
        """

        Args:
            self (Director): An instance of Director.
        """