class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    
    
    def draw_picture(self, parachute, letters):

        for line in parachute:
            print(line)
        
        print()
        for letter in letters:
            print(letter, end=' ')
        print()
        # space = ''
        # for i in letters:
        #     word = space + " " + i
        #     print(word)

    def read_text(self):
    
        letter = 'Fantastic'
        while len(letter) > 1:
            letter = input('Guess a letter: ')
        return letter
            
    def display_end_game(self, master_word, lives):  
        if lives > 0:
            print(f"well done word smith, you've won with {lives} lives left.")
        elif lives <= 0:
            print(f'You are no word smith, the correct word was {master_word}')