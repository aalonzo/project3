try:
    from Tkinter import * 
    #Entry, Frame, Label, StringVar
    from Tkconstants import *
except ImportError:
    from tkinter import *
    from tkinter.constants import *

from PIL import ImageTk, Image
from professor import *
#from class_creation import *
import sys
import os.path
import turtle

SUITE_TITLE = "LearnIt"
PROGRAM = "Gradebook"
PROG_TITLE = SUITE_TITLE + " " + PROGRAM


class Gradebook:
	def __init__(self, master):
		self.window = master
		self.window.geometry("800x600")
		self.window.title(PROG_TITLE)

		self.setup()
		self.get_data()

	def setup(self):
		header = Label(self.window, text=PROG_TITLE, font=('Arial', 28), bg="#bf5700", fg="white", anchor="nw", padx=5, pady=10, justify=LEFT)
		header.pack(side=TOP, anchor="nw", fill="x")

		self.setup_no_classes_objects()

	def setup_no_classes_objects(self):
		self.text = Label(self.window, text="Welcome to the Gradebook application!\nNo classes have been added.  Use the Create Schedule wizard to add classes to your schedule.", fg="black")

		self.bottom_button_frame = Frame(self.window, background="", width=100)

		self.make_schedule = Button(self.bottom_button_frame, text="Create Schedule", command=lambda: [self.wizard()])
		self.close_module = Button(self.bottom_button_frame, text="Close Program", command=lambda: self.window.destroy())

	def wizard(self):
		wizard_win = Toplevel(self.window)
		wizard_win.geometry("650x600")
		wizard_win.title(PROG_TITLE)
		self.wizard_header = Label(wizard_win, text=" Create Schedule Wizard", font=('Arial', 28), bg="#bf5700", fg="white", anchor="nw", padx=5, pady=10, justify=LEFT)
		self.wizard_header.pack(side=TOP, anchor="nw", fill="x")

		self.wizard_page1(wizard_win)

	def wizard_page1(self, wizard_win):
		self.text = Label(wizard_win, wraplength=600, text="This wizard will guide you through the creation of your schedule.\nClick \"Next\" to continue, or \"Cancel\" to close the wizard.", fg="black")
		self.wizard_button_frame = Frame(wizard_win, background="", width=25)

		self.next = Button(self.wizard_button_frame, text="Cancel", command=lambda: [wizard_win.destroy()])
		self.cancel = Button(self.wizard_button_frame, text="Next", command=lambda: self.wizard_page2(wizard_win))

		self.wizard_button_frame.pack(side=BOTTOM, padx=50, pady=50, ipadx=20, anchor="e")
		self.text.pack(side=TOP, pady=50)
		self.next.pack(side=LEFT, ipadx=5, ipady=5)
		self.cancel.pack(side=RIGHT, ipadx=5, ipady=5)

	def wizard_page2(self, wizard_win):
		self.text.config(text="How many classes are you adding?  Enter this number below.")
		self.wizard_header.config(text=" Create Schedule Wizard (Step 1)")
		self.entry_field = Entry(wizard_win, text="Enter a number here.")
		self.entry_field.pack(side=TOP)

		self.next.config(command=lambda: [wizard_win.destroy()])
		self.cancel.config(command=lambda: self.wizard_page3(wizard_win))

	def wizard_page3(self, wizard_win):
		self.text.config(text="Enter the course numbers below.\nThe format for a course number is the department initial(s), followed by the number and a letter, if applicable (e.g., CS313E).")
		self.wizard_header.config(text=" Create Schedule Wizard (Step 3)")

		self.next.config(command=lambda: [wizard_win.destroy()])
		self.cancel.config(command=lambda: self.wizard_page4(wizard_win))

		try:
			self.num_classes = int(self.entry_field.get())
		except ValueError:
			print("egg")
			#messagebox.info("You must enter an integer for the number of classes.")
		else:	
			self.entry_field.delete(0, END)
			self.entry_field.destroy()

			self.frames =[]
			self.labels = []
			self.entries = []

			for i in range(self.num_classes):
				frame = Frame(wizard_win, background="")
				self.frames.append(frame)
				frame.pack(side=TOP)

				label = Label(frame, text="Course " + str(i+1) + ":" )
				self.labels.append(label)
				label.pack(side=LEFT)
				entry = Entry(frame)
				self.entries.append(entry)
				entry.pack(side=TOP)

	def wizard_page4(self, wizard_win):
		self.text.config(text="What time does each class start and end?  Enter them below.")
		self.wizard_header.config(text=" Create Schedule Wizard (Step 4)")

		table_frame = Frame(wizard_win, background="")
		table_frame.pack(side=TOP)

		start_label = Label(table_frame, text="Start")
		end_label = Label(table_frame, text="End")
		start_label.pack(side=LEFT, padx=15)
		end_label.pack(side=RIGHT, padx=30)

		self.next.config(command=lambda: [wizard_win.destroy()])
		self.cancel.config(command=lambda: self.wizard_page5(wizard_win), start_label.destroy(), end_label.destroy(), table_frame.destroy())

		self.inputs = []

		for i in range(len(self.entries)):
			self.labels[i].destroy()
			self.inputs.append(str(self.entries[i].get()))
			print(self.inputs[i])
			self.entries[i].destroy()
			self.frames[i].destroy()

		print(self.inputs)

		self.frames =[]
		self.labels = []
		self.entries = []

		for j in range(len(self.inputs)):
			#print(str(self.inputs[j].get()))
			frame = Frame(wizard_win, background="")
			frame.pack(side=TOP)
			label = Label(frame, text=str(self.inputs[j]) + ":" )
			label.pack(side=LEFT)
			start_time = Entry(frame, width=20)
			start_time.pack(side=LEFT)
			end_time = Entry(frame, width=20)
			end_time.pack(side=RIGHT)

		# for j in range(len(self.inputs)):
		# 		print("element ", str(j+1), str(self.inputs[j].get()))

	def wizard_page5(self, wizard_win):
		return None

	def show_no_classes_screen(self):
		self.text.pack(side=TOP, pady=50)
		self.bottom_button_frame.pack(side=BOTTOM, pady=50, ipadx=20)
		self.make_schedule.pack(side=LEFT, ipadx=5, ipady=5)
		self.close_module.pack(side=RIGHT, ipadx=5, ipady=5) 

	def unshow_no_class_widgets(self):
		self.text.pack_forget()
		self.bottom_button_frame.pack_forget()
		self.make_schedule.pack_forget()
		self.close_module.pack_forget()

	def get_data(self):
		# check if file exists
		file_exists = os.path.isfile("classes.csv")
		if file_exists:
			print("do things")
		elif not file_exists:
			self.show_no_classes_screen()
		# check if person has saved any classes within .csv file



root = Tk()
my_gui = Gradebook(root)
root.mainloop()