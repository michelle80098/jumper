class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    
    
    def draw_picture(self, parachute, letters):
        for i in letters:
            word = letters + " " + i
            print(word)
        # for line in parachute:
        #     print(line)
        # print(letters)
        # TODO For loop to display the letters list in draw_picture

    def read_text(self):
        letter = None
        while type(letter) != str and 0 >= len(letter) > 1:
                letter = input('Guess a letter: ')
        return letter
            
    def display_end_game(self, master_word, lives):
        # TODO Director will be giving you all of the information that you need
        
        if lives > 0:
            print(f"well done word smith, you've won with {lives} left.")
        elif lives <= 0:
            print(f'You are no word smith, the correct word was {master_word}')


        # Information passed will be the number of lives remaining. If you have more than 0 lives remaining
        # then you won. In both cases whether you have won or lost you will be given remaining lives (an int)
        # the letters making up THE WORD that was randomly selected as a (list) 
        # The second will contain dashes and guessed letters, this may have empty spaces in it
        # if they didn't guess everything correctly (Also a List)
        
        # TODO print endgame information
        
        # a change
