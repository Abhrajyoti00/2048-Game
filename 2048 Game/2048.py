from tkinter import *

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
        #Path of the Game Logo
        photo = PhotoImage(file = "D:\\Documents\\Python Learning Plus\\PROGRAMS\\2048 Game Project\\2048 Game\\Img\\GameIcon.png")
        self.master.iconphoto(False, photo)
        

        self.grid()   #Tkinter has grid manager, which allows to create grid
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down) #Bind the frame with the key
        
        self.commands = {c.KEY_UP: Logics.move_up, c.KEY_DOWN: Logics.move_down,
        c.KEY_LEFT: Logics.move_left, c.KEY_RIGHT: Logics.move_right, c.KEY_UP_ALT: Logics.move_up, c.KEY_DOWN_ALT: Logics.move_down,
                         c.KEY_LEFT_ALT: Logics.move_left, c.KEY_RIGHT_ALT: Logics.move_right}

        Frame.focus_set(self) #Moves the keyboard focus to the frame
        self.grid_cells = []
        self.init_grid()  #Initializes the Grid by addiing the grid cells
        self.init_matrix() #Initializes the Matrix by adding new 2's in the matrix after starting the game
        self.update_grid_cells() #Changes background and text color. (UI Changes)

        self.mainloop()   # Actually runs the program
        


    #INITIALIZING THE GRID

    def init_grid(self):
        
        '''
        Now we create another Frame within the frame, with the color and sizes given under the constants.py file
        '''
        
        background = Frame(self, bg = c.BACKGROUND_COLOR_GAME, width = c.SIZE, height = c.SIZE)
        
        background.grid()   #Visualizing the background as a grid

        #Now we need to add cells

        for i in range(c.GRID_LEN):
            grid_row = []   #Each row of Grid
            for j in range(c.GRID_LEN):
                #Here  the cell is created with sizes (400/4) = 100. Cell itself is a frame
                cell = Frame(background, bg = c.BACKGROUND_COLOR_CELL_EMPTY, width = c.SIZE/c.GRID_LEN, height = c.SIZE/c.GRID_LEN) 
                
                cell.grid(row = i, column = j, padx = c.GRID_PADDING, pady = c.GRID_PADDING) # Adding a  cell at (i,j) with padding = 10
                #Padding is the space between the cells
                                 
                t = Label(master=cell, text = '', bg = c.BACKGROUND_COLOR_CELL_EMPTY, 
                justify = CENTER, font = c.FONT, width = 5, height = 2)  # Creating the label in the grid. By default the text is empty
                t.grid()  
                #Label covers  the cell completely. Just the label will get change. So we will append only the label.
                grid_row.append(t) 

            self.grid_cells.append(grid_row)  #Rows of Labels. In each grid cells there are labels. 

    
    #INITIALIZING THE MATRIX 

    ''' Our UI Part is Completed. Now our task is to visualize them with the help of our matrix'''

    def init_matrix(self):
        self.matrix = Logics.start_game()   #Returns a 2d Matrix with all values 0. Using this we will reflect on UI
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]  #Storing the current value of matrix at (i,j) in new_number
                if new_number == 0: #Empty so no need to update the UI Text
                    self.grid_cells[i][j].configure(text = "", bg = c.BACKGROUND_COLOR_CELL_EMPTY)  #Query or set the default value of the specified option(s) in style.
                else:
                    self.grid_cells[i][j].configure(text = str(new_number), bg = c.BACKGROUND_COLOR_DICT[new_number], fg = c.CELL_COLOR_DICT[new_number])

        self.update_idletasks()   # It is in the frame library. It will wait until all the color changes.

    # What happens when we Press a Key?

    def key_down(self, event):  #Here event is what key we have pressed

        '''
        Keys are assigned using Keycodes defined in constants.py file

        # WASD Keys event in details :-

        <KeyPress event state=Mod1 keysym=d keycode=68 char='d' x=1407 y=-8>
        <KeyPress event state=Mod1 keysym=s keycode=83 char='s' x=1407 y=-8>
        <KeyPress event state=Mod1 keysym=w keycode=87 char='w' x=1407 y=-8>
        <KeyPress event state=Mod1 keysym=a keycode=65 char='a' x=1407 y=-8>

        # Arrow Keys event in details :-

        <KeyPress event state=Mod1|0x40000 keysym=Down keycode=40 x=1407 y=-8>
        <KeyPress event state=Mod1|0x40000 keysym=Left keycode=37 x=1407 y=-8>
        <KeyPress event state=Mod1|0x40000 keysym=Up keycode=38 x=1407 y=-8>
        <KeyPress event state=Mod1|0x40000 keysym=Right keycode=39 x=1407 y=-8>

        '''

        key = event.keycode  # We extract the keycode part (an integer)

        if key in self.commands:
            self.matrix, changed = self.commands[event.keycode](self.matrix)   #Command maps the key, makes the movement in the matrix
            
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()  #Updating the grid cells
                changed = False # It should be false by default 
                if Logics.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text = "YOU", bg = c.BACKGROUND_COLOR_DICT["YOU WON"], fg = c.CELL_COLOR_DICT["Result"])
                    self.grid_cells[1][2].configure(text = "WIN!", bg = c.BACKGROUND_COLOR_DICT["YOU WON"], fg = c.CELL_COLOR_DICT["Result"])
                    
                if Logics.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text = "YOU", bg = c.BACKGROUND_COLOR_DICT["YOU LOST"], fg = c.CELL_COLOR_DICT["Result"])
                    self.grid_cells[1][2].configure(text = "LOSE!", bg = c.BACKGROUND_COLOR_DICT["YOU LOST"], fg = c.CELL_COLOR_DICT["Result"])
                    


gamegrid = Game2048()





