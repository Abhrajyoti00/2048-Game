from tkinter import Frame, Label, CENTER

import Logics
import constants as c

class Game2048(Frame):  
    '''
    Frame is the Superclass
    It works like a container, which is responsible 
    for arranging the position of other widgets.
    '''
    
    def __init__(self):  # Constructor
        Frame.__init__(self)
        self.grid()   #Tkinter has grid manager, which allows to create grid
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down) #Bind the frame with the key
        self.commands = {c.KEY_UP: Logics.move_up, c.KEY_DOWN: Logics.move_down,
        c.KEY_LEFT: Logics.move_left, c.KEY_RIGHT: Logics.move_right}

        self.grid_cells = []
        self.init_grid()  #Initializes the Grid by addiing the grid cells
        self.init_matrix() #Initializes the Matrix by adding new 2's in the matrix after starting the game
        self.update_grid_cells() #Changes backgroud and text color. (UI Changes)

        self.mainloop()   # Actually runs the program
        

