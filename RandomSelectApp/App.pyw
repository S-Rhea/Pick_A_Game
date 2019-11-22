from MyGUI import myGui
from tkinter import *


app = Tk()
app.geometry('300x300')
gui = myGui(app)
gui.raise_frame(gui.main_frame)
app.mainloop()
