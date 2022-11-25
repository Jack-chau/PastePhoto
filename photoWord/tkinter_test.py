
import tkinter as tk
from tkinter import *

# launch window
window = tk.Tk ( )

# Window name
window.title ( "first_try" )

# Set size
window.minsize ( width = 400, height = 200 )

# Set resizable
window.resizable ( True, True ) # width, height

# Define button variable
button_var = IntVar ( ) # Integer type variable
button_var.set ( 1 )

# Button
button_A = Radiobutton ( window )
button_A.config ( text = "A", variable = button_var, value = 1 )

button_B = Radiobutton ( window )
button_B.config ( text = "B", variable = button_var, value = 2 )

button_run = Button ( window, text = "Run" )
# Change button color
# button_A.config = ( bg = "skyblue" )

button_A.config ( width = 10, height = 3 )
button_B.config ( width = 10, height = 3 )
button_run.config ( width = 10, height = 5)

# show button on screen
button_A.pack ( )
button_B.pack ( )
button_run.pack ( )

window.mainloop ( )

