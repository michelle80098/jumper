from doctest import master
from xmlrpc.client import boolean
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

        """ Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
            
        """
        
    def start_game(self):
        master_word = self.words.word_select()
        self.master_word = master_word
        drawing, word_dashes = self.jumper.create_drawing(self.master_word)
        self.terminal_service.draw_picture(drawing, word_dashes)

        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        letter = self.terminal_service.read_text('Guess a letter: ')
        self.letter = letter
        
    def _do_updates(self):
        boolean = self.words.compare_words(self.letter)
        assert type(boolean) == bool
        self.jumper.guess(boolean, self.letter)
        drawing, word_dashes = self.jumper._update_drawing()
        self.drawing, self.word_dashes = drawing, word_dashes
        

        """

        Args:
            self (Director): An instance of Director.
        """
        
    def _do_outputs(self):
        self.terminal_service.draw_picture(self.drawing, self.word_dashes)

        #TODO Lives: Which class would take care of that?
        """

        Args:
            self (Director): An instance of Director.
        """
