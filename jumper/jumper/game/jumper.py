class Jumper:
    #  must have attributes (any global variable) will need __init__(self)
    def __init__(self):
        self._the_word = None
        self._dashes = []
        self._parachute
    def create_drawing(self, word):

        line_1 = " ___  "
        line_2 = "/___\ "
        line_3 = "\   / "
        line_4 = " \ /  "
        line_5 = "  o   "
        line_6 = " /|\  "
        line_7 = " / \  "
        
        self.parachute = [line_1, line_2, line_3, line_4, line_5, line_6, line_7] 

        self._the_word = word
        number_of_dashes = len(self._the_word)
        for n in number_of_dashes:
            self._dashes.append("_") 
        
        return self._parachute, self._dashes

    # take input from user from Director class 
    def guess(self, boolean, user_letter):
        if boolean == True:
            for letter in self._the_word:
                if user_letter == letter:
                    self._dashes.replace(letter)
        else:
            self.update_drawing(self)

    def winner(self):
        if "_" not in self._dashes:
            return True
        else:
            return False


    # update drawing based on inp
    def update_drawing(self):
        self._parachute[0] 
        # return list of drawing at the end of update drawing method
        