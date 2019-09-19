'''
The GUI view for the Calvin Story game
Author: Young Kwang Park

Portions of the CountryGuessGame made by Professor Keith Vander Linden, of Calvin College
were referenced to help build this GUI
'''
from tkinter import *

from CalvinStory import Game

'''I need to make the main frame outside as a global variable in order to manipulate it later on the
list of local variables in order to change the images shown in the labels.'''
root = Tk()
root.title('Calvin Story')
    
main_frame = Frame()
main_frame.pack(padx=10, pady=10)
label_font = ('Helvetica') 
       
logo = PhotoImage(file='images/introduction.gif')
image_label = Label(main_frame, image=logo, height=550, width=1500)
image_label.image = logo
image_label.pack()

class App:
    
    def __init__(self, window):

        self._game = Game()
        '''Creates the dialog box where instructions and dialogue is given to the player'''
        self._text_variable = StringVar()
        self._text_variable.set("Press A to continue".format(self._game.get_b()))
        game_label = Label(main_frame, textvariable=self._text_variable, font=label_font, wraplength = 900)
        game_label.pack(anchor="center")
                
        input_frame = Frame(main_frame)
        input_frame.pack(anchor=CENTER, fill=X)

        '''Creates both A and B buttons'''
        a_button = Button(input_frame, text='A', command=self.button_a, font=label_font, height = 1, width = 10)
        a_button.pack(side=LEFT, padx=5)
        b_button = Button(input_frame, text='B', command=self.button_b, font=label_font, height = 1, width = 10)
        b_button.pack(side=LEFT, padx=5)
        
        '''Creates an Education label'''
        self._education_variable = StringVar()
        self._education_variable.set("Education: {0}".format(self._game.education))
        education_label = Label(input_frame, textvariable=self._education_variable, font=label_font, height = 1, width = 15)
        education_label.pack(side=LEFT, padx=5)
        
        '''Creates a Social label'''
        self._education_variable2 = StringVar()
        self._education_variable2.set("Social: {0}".format(self._game.social))
        social_label = Label(input_frame, textvariable=self._education_variable2, font=label_font, height = 1, width = 15)
        social_label.pack(side=LEFT, padx=5)
        
        '''Creates a Love label'''
        self._love_variable = StringVar()
        self._love_variable.set("Love: {0}".format(self._game.love))
        social_label = Label(input_frame, textvariable=self._love_variable, font=label_font, height = 1, width = 15)
        social_label.pack(side=LEFT, padx=5)
        
        '''Create a quit button'''
        quit_button = Button(input_frame, text='Quit', command=main_frame.quit, font=label_font, fg = "red")
        quit_button.pack(side=RIGHT)
    
    '''Defining what the button A should be doing. It's capable of updating the status labels and 
    the images shown in the labels'''
    def button_a(self, event=None):
        
        a = self._game.get_a()
        c = self._game.get_education()
        e = self._game.get_social()
        g = self._game.get_love()
        self._text_variable.set(format(a))
        self._education_variable.set("Education: {0}".format(c))
        self._education_variable2.set("Social: {0}".format(e))
        self._love_variable.set("Love: {0}".format(g))

        logo2 = PhotoImage(file=self._game.change_pic())
        image_label.configure(image=logo2)
        image_label.image = logo2
        image_label.pack()
     
    '''Defining what the button B should be doing. It's capable of updating the status labels'''        
    def button_b(self, event=None):

        b = self._game.get_b()
        d = self._game.get_education()
        f = self._game.get_social()
        h = self._game.get_love() 
        self._text_variable.set(format(b))
        self._education_variable.set("Education: {0}".format(d))
        self._education_variable2.set("Social: {0}".format(f))
        self._love_variable.set("Love: {0}".format(h))
        
if __name__ == '__main__':
    app = App(root)
    root.mainloop()