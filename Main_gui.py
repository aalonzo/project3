from tkinter import *

root = Tk()
root.geometry("800x600")
root.title(string="Main Menu")
frame = Frame(root)
frame.pack()

bottomframe = Frame(root, bg = "#bf5700")
bottomframe.pack(ipadx=800, ipady = 15, side = BOTTOM)

redbutton = Button(bottomframe, text = "Professors", fg = "white", bg = "#f8971f")
redbutton.pack(ipadx = 10, ipady = 10, side = LEFT, anchor = CENTER)


greenbutton = Button(bottomframe, text = "Classes", fg = "white", bg = "#f8971f")
greenbutton.pack(ipadx = 10, ipady = 10, side = LEFT, anchor = CENTER)

bluebutton = Button(bottomframe, text = "Grades", fg = "white", bg = "#f8971f")
bluebutton.pack(ipadx=10, ipady = 10, side = LEFT, anchor = CENTER)

root.mainloop()
