from tkinter import *

root = Tk()
root.geometry("800x600")
frame = Frame(root)
frame.pack()

bottomframe = Frame(root, bg = "blue")
bottomframe.pack(ipadx=800, ipady = 15, side = BOTTOM)

redbutton = Button(bottomframe, text = "Professors", fg = "green", bg = "green")
redbutton.pack(ipadx = 10, ipady = 10, side = LEFT, anchor = CENTER)


greenbutton = Button(bottomframe, text = "Classes", fg = "green", bg = "green")
greenbutton.pack(ipadx = 10, ipady = 10, side = LEFT, anchor = CENTER)

bluebutton = Button(bottomframe, text = "Grades", fg = "green", bg = "green")
bluebutton.pack(ipadx=10, ipady = 10, side = LEFT, anchor = CENTER)

root.mainloop()
