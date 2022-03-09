class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def draw_picture(self, parachute, letters):
        for line in parachute:
            print(line)
        print(letters)

    def read_text(self, needed_info):
        if needed_info == 'Guess a letter: ':
            letter = None
            while type(letter) != str and 0 >= len(letter) > 1:
                    letter = input(needed_info)
            return letter
        else:
            # TODO print endgame information
            pass