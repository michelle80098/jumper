class Jumper:
    #  must have attributes (any global variable) will need __init__(self)
    def __init__(self):
        pass
    def create_drawing(self, word):

        line_1 = " ___  "
        line_2 = "/___\ "
        line_3 = "\   / "
        line_4 = " \ /  "
        line_5 = "  o   "
        line_6 = " /|\  "
        line_7 = " / \  "
        
        self.parachute = [line_1, line_2, line_3, line_4, line_5, line_6, line_7] 

        
        list_of_letters = list(word)
        number_of_dashes = len(list(word))
        
        # return self.parachute 


    # take input from user from Director class 
    def guess(self, boolean, letter):
        if boolean == True:
            

    # update drawing based on inp
    def _update_drawing(self):
        pass
        # return list of drawing at the end of update drawing method
        