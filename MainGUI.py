''' author: Adrian Alonzo, Raleigh Melancon, Sally, Ryan, Sunny, Jonathon, Nick, Luis.
	filename: Example.py
	purpose: to demonstrate how to superimpose a text field and buttons
			 on top of a scene, as well as hide/show the text field.
'''

from tkinter import *
from PIL import ImageTk,Image
import os.path
import io
from search import *
from Gradebook import *


# some global variables for us to use throughout the program.
BUTTON_SPACING = 50
INSTALL_DIR = os.getcwd() + "/"
WINDOW_TITLE = "Start Page"
WINDOW_WIDTH = "720"
WINDOW_HEIGHT = "1024"
WINDOW_COLOR = '#BEBEBE'

# this function updates the status bar to whatever we want.
# we have to update the text with an empty string first and then
# call update_idletasks() method to update the status bar correctly.
# then we set the text to whatever we ewant and it does it!
def update_status_bar(status_text_widget, sb_text):
	status_text_widget.config(text="")
	status_text_widget.update_idletasks()
	status_text_widget.config(text=sb_text)
	status_text_widget.update_idletasks()
	


# this function updates the text box to whatever we want.
# to make it read only, we have to set the state to normal so the text can be edited.
# according to the documentation, you delete text by specifying the arguments below.
# once written, you set the state to disabled, giving you a read-only dialog box!
def update_text_box(dialog_widget, text_dialog):
	dialog_widget.configure(state='normal') 
	dialog_widget.delete(1.0, END)
	dialog_widget.insert(END, text_dialog)
	dialog_widget.configure(state='disabled') 

# method for updating image given the widget for background iamge, the image's filename 
# (with extension), and text you want to show in the dialog box for this scene.
def update_scene(bg_image_widget, button_frame, dialog_widget, sb_widget, image_name, text_dialog, sb_text):
	# update the text using the above function.
	update_status_bar(sb_widget, sb_text)
	update_text_box(dialog_widget, text_dialog)

	# button_frame.pack(side="bottom", anchor="s", pady=50)
	# dialog_widget.pack(side="bottom", anchor="s", fill="none", ipadx=5, ipady=5)

	# the standard image opening code used in the last release.
	img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + image_name))
	bg_image_widget.config(image=img)
	bg_image_widget.image=img

	button_frame.configure(background="")
	button_frame.update()


# method to hide the text box.  to give the appearance of hiding it within the same scene,
# pass the same background image placed under the dialog box, and an empty string ("", NOT None)
# for the dialog.  
def hide_text_box(bg_image_widget, button_frame, dialog_widget, sb_widget, image_name, text_dialog, sb_text):
	dialog_widget.pack_forget()
	update_scene(bg_image_widget, button_frame, dialog_widget, sb_widget, image_name, text_dialog, sb_text)

# method to show the text box.
# as you can see, it's basically the reverse of the hide_text_box function.
# should be self-explanatory, but if not, feel free to ask questions.
def show_text_box(bg_image_widget, button_frame, dialog_widget, sb_widget, image_name, text_dialog, sb_text):
	dialog_widget.pack(side="bottom", anchor="s", fill="none", ipadx=5, ipady=5)
	update_scene(bg_image_widget, button_frame, dialog_widget, sb_widget, image_name, text_dialog, sb_text)
	
def show_scheduler():
	root = Tk()
	my_gui = Gradebook(root)
	root.mainloop()

def main():
	window = Tk() # create window
	window.title(WINDOW_TITLE)
	window.geometry(WINDOW_HEIGHT+"x"+WINDOW_WIDTH) # set window dimensions

	# this makes a Label widget for the image to go on.  
	# using the Place method, we are able to make it the background image on the window.
	bg_image = Label(window)
	bg_image.place(relx=0.5, rely=0.5, anchor=CENTER)

	status_bar = Label(window, bd=1, text="", anchor="w", relief=SUNKEN, background=WINDOW_COLOR)
	# status_bar.pack(side="bottom", fill="x", anchor="s")
	# the widget for the dialog box.  I've specified a width and height for it here, 
	# but we can adjust it accordingly depending on the scene.
	dialog_box = Text(window, bd=10, highlightbackground="black", height=10, width=80)
	
	# frame for the buttons.  made so they can be all on the same line.
	# the background has been filled with red to demonstrate how the frame
	# is laid onto the window.
	bottom_button_frame = Frame(window, background="", width=100)

	
	# the starting image for the scene, along with the initial dialog we want to show.
	update_scene(bg_image, bottom_button_frame, dialog_box, status_bar, "home.png", "Hi, I'm playing on the right side of the backyard!", "Max is on the right.")

	# status_bar.pack(side="bottom", fill="x", expand=True)
	# these are the buttons for this demo.
	# using the functions above, I am able to update the scene accordingly
	# and/or hide/show the text box by assigning the appropriate functions to their commands.
	# each function's functionality will be explaind above.
	prev = Button(text="Schedule", command=lambda: [window.destroy(), show_scheduler()],  fg = "white", bg = "#f8971f")
	next = Button(text="Professors", command=lambda: [window.destroy(), searchProg()],  fg = "white", bg = "#f8971f")
	#other = Button(text="Grades", command=lambda: [window.destroy(), professor()], fg = "white", bg = "#f8971f")
	
	# pack the buttons in the container. 
	# since we want them to be in the bottom frame, we use in_ to achieve this.
	# we then do some magic with padding to get the configuration you'll see in the window.
	next.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
# 	other.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)

	prev.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)


	# pack the frame we made onto the window
	bottom_button_frame.pack(side="bottom", anchor="s", pady=50)

	
	window.mainloop()

main()
