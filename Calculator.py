from tkinter import *
from buttonPress import *

number = ""

class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Calculator")

        # create frame for display
        frameDisplay = Frame(window).pack()

        # create and place label widget for displaying calculations
        display = Label(frameDisplay, text = number)

        # create frame for buttons
        frameButtons = Frame(window)
        frameButtons.pack() # pack button frame into window
        
        # place buttons 1-0 in button frame using grid manager
        button1 = Button(frameButtons, text = "1",
                    command = buttonPress1(number))
        button1.grid(row = 1, column = 1, padx = 5, pady = 5)

        button2 = Button(frameButtons, text = "2",
                    command = buttonPress2(number))
        button2.grid(row = 1, column = 2, padx = 5, pady = 5)

        button3 = Button(frameButtons, text = "3", command = buttonPress3)
        button3.grid(row = 1, column = 3, padx = 5, pady = 5)

        button4 = Button(frameButtons, text = "4", command = buttonPress4)
        button4.grid(row = 2, column = 1, padx = 5, pady = 5)

        button5 = Button(frameButtons, text = "5", command = buttonPress5)
        button5.grid(row = 2, column = 2, padx = 5, pady = 5)
        
        button6 = Button(frameButtons, text = "6", command = buttonPress6)
        button6.grid(row = 2, column = 3, padx = 5, pady = 5)

        button7 = Button(frameButtons, text = "7", command = buttonPress7)
        button7.grid(row = 3, column = 1, padx = 5, pady = 5)

        button8 = Button(frameButtons, text = "8", command = buttonPress8)
        button8.grid(row = 3, column = 2, padx = 5, pady = 5)

        button9 = Button(frameButtons, text = "9", command = buttonPress9)
        button9.grid(row = 3, column = 3, padx = 5, pady = 5)

        button0 = Button(frameButtons, text = "0", command = buttonPress0)
        button0.grid(row = 4, column = 2, padx = 5, pady = 5)

        # place buttons +, -, *, / in button frame using grid manager
        buttonAdd = Button(frameButtons, text = "+",
                        command = buttonPressAdd).grid(row = 1,
                        column = 4, padx = 10, pady = 5)
        buttonSub = Button(frameButtons, text = "-",
                        command = buttonPressSub).grid(row = 2,
                        column = 4, padx = 10, pady = 5)
        buttonMul = Button(frameButtons, text = "*",
                        command = buttonPressMul).grid(row = 3,
                        column = 4, padx = 10, pady = 5)
        buttonDiv = Button(frameButtons, text = "/",
                        command = buttonPressDiv).grid(row = 4,
                        column = 4, padx = 10, pady = 5)
    
        # create event loop
        window.mainloop()


Calculator() # create GUI
