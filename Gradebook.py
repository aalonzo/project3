try:
    from Tkinter import * 
    #Entry, Frame, Label, StringVar\
    from Tkconstants import *
    from Tkinter import messagebox
except ImportError:
    from tkinter import *
    from tkinter.constants import *
    from tkinter import messagebox

from PIL import ImageTk, Image
from professor import *
#from class_creation import *
import sys
import os.path
import turtle

SUITE_TITLE = ""
PROGRAM = "Scheduler"
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
		self.text = Label(self.window, text="Welcome to the Scheduler application!\nNo classes have been added.  Use the Create Schedule wizard to add classes to your schedule, or load a previously saved one.", fg="black", wraplength=600)
		self.bottom_button_frame = Frame(self.window, background="", width=100)

		#self.make_schedule = Button(self.bottom_button_frame, text="Create Schedule", command=lambda: [self.init_wizard()])

		self.make_schedule = Button(self.bottom_button_frame, text="Create Schedule", command=lambda: [self.init_wizard()])
		self.load = Button(self.bottom_button_frame, text="Load Schedule", command=lambda: [self.load_schedule()])
		self.close_module = Button(self.bottom_button_frame, text="Close Program", command=lambda: self.window.destroy())

	def load_schedule(self):
		self.unshow_no_class_widgets()
		#;)
		#self.window.after(5000, self.show_schedule())
		self.show_schedule()


	def show_schedule(self):
		schedule_name = Label(self.window, text="Jane Doe's Schedule", font=('Arial', 16), fg="black", padx=5, pady=10, justify=LEFT)
		schedule_name.pack(side=TOP, anchor="nw")
		table_header_frame = Frame(self.window)
		table_header_frame.pack(side=TOP, anchor="nw", padx=50, pady=5)




		class_header = Label(table_header_frame, text="Class", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		class_header.pack(side=LEFT, anchor="nw")
		time_header = Label(table_header_frame, text="Time", font=('Arial', 14), fg="black", padx=50, pady=10, justify=LEFT)
		time_header.pack(side=LEFT, anchor="nw")
		prof_header = Label(table_header_frame, text="Professor", font=('Arial', 14), fg="black", padx=145, pady=10, justify=LEFT)
		prof_header.pack(side=LEFT, anchor="nw")
		prof_header = Label(table_header_frame, text="Difficulty", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		prof_header.pack(side=LEFT, anchor="nw")



		schedule_frame = Frame(self.window, bd=2)
		schedule_frame.pack(side=TOP, anchor="nw", padx=50, pady=15)

		class1_frame = Frame(schedule_frame)
		class1_frame.pack(side=TOP, anchor="w")
		class2_frame = Frame(schedule_frame)
		class2_frame.pack(side=TOP, anchor="w")
		class3_frame = Frame(schedule_frame)
		class3_frame.pack(side=TOP, anchor="w")
		class4_frame = Frame(schedule_frame)
		class4_frame.pack(side=TOP, anchor="w")

		class1 = Label(class1_frame, text="AST301", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		class1.pack(side=LEFT, anchor="nw")

		time1 = Label(class1_frame, text="TTH, 12:30 PM to 2:00 PM", font=('Arial', 14), fg="black", padx=40, pady=10, justify=LEFT)
		time1.pack(side=LEFT)
		prof1 = Label(class1_frame, text="Donald Winget", font=('Arial', 14), fg="black", padx=15, pady=10, justify=LEFT)
		prof1.pack(side=LEFT)
		diff1 = Label(class1_frame, text="2.9", font=('Arial', 14), fg="black", padx=95, pady=10, justify=LEFT)
		diff1.pack(side=LEFT)

		other_button_frame = Frame(self.window)
		other_button_frame.pack(side=BOTTOM, pady=50)
		# add_button = Button(other_button_frame, text="Add Class", padx=5, pady=5, command=lambda: self.add_to_schedule())
		# add_button.pack(side=BOTTOM)



		class2 = Label(class2_frame, text="SOC379M", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		class2.pack(side=LEFT, anchor="nw")
		time2 = Label(class2_frame, text="TTH, 2:00 PM to 3:30 PM", font=('Arial', 14), fg="black", padx=25, pady=10, justify=RIGHT)
		time2.pack(side=LEFT)
		prof2 = Label(class2_frame, text="Ari Adut", font=('Arial', 14), fg="black", padx=40, pady=10, justify=LEFT)
		prof2.pack(side=LEFT)
		diff2 = Label(class2_frame, text="2.3", font=('Arial', 14), fg="black", padx=300, pady=10, justify=LEFT)
		diff2.pack(side=LEFT)
		class4 = Label(class4_frame, text="SOC317L", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		class4.pack(side=LEFT, anchor="nw")
		time4 = Label(class4_frame, text="MWF, 11:00 AM to 12:30 PM", font=('Arial', 14), fg="black", padx=35, pady=10, justify=RIGHT)
		time4.pack(side=LEFT)
		prof4 = Label(class4_frame, text="Ken-Hou Lin", font=('Arial', 14), fg="black", padx=5, pady=5, justify=LEFT)
		prof4.pack(side=LEFT)
		diff4 = Label(class4_frame, text="1.8", font=('Arial', 14), fg="black", padx=500, pady=10, justify=LEFT)
		diff4.pack(side=LEFT)
		average_frame = Frame(self.window)
		average_frame.pack(side=TOP)
		average= Label(average_frame, text="Semester Difficulty (Avg of Prof. Difficulties): 2.3", font=('Arial', 14), fg="black", padx=5, pady=10, justify=LEFT)
		average.pack(side=LEFT)

	def add_to_schedule(self):
		self.addwin = Toplevel(self.window)
		self.addwin.geometry("800x600")

		header = Label(self.addwin, text="  Add Class", font=('Arial', 28), bg="#bf5700", fg="white", anchor="nw", padx=5, pady=10, justify=LEFT)
		header.pack(side=TOP, anchor="nw", fill="x")

		addwin.mainloop()


	def init_wizard(self):
		wizard = Wizard(self.window)

	def show_no_classes_screen(self):
		self.text.pack(side=TOP, pady=50)
		self.bottom_button_frame.pack(side=BOTTOM, pady=50, ipadx=20)
		self.make_schedule.pack(side=LEFT, padx=5, ipadx=5, ipady=5)
		self.load.pack(side=LEFT, padx=5, ipadx=5, ipady=5)
		self.close_module.pack(side=LEFT, padx=5, ipadx=5, ipady=5) 

	def unshow_no_class_widgets(self):
		self.text.pack_forget()
		self.bottom_button_frame.pack_forget()
		self.make_schedule.pack_forget()
		self.load.pack_forget()
		self.close_module.pack_forget()

	def get_data(self):
		# check if file exists
		file_exists = os.path.isfile("classes.csv")
		if file_exists:
			print("do things")
		elif not file_exists:
			self.show_no_classes_screen()
		# check if person has saved any classes within .csv file

class Wizard:
	def __init__(self, master):
		self.window = Toplevel(master)
		self.wraplength = 650
		self.window.geometry(str(self.wraplength) +"x600")
		self.window.title("Schedule Creation Wizard")
		self.wizard_header = Label(self.window, text=" Create Schedule Wizard", font=('Arial', 28), bg="#bf5700", fg="white", anchor="nw", padx=5, pady=10, justify=LEFT)
		self.wizard_header.pack(side=TOP, anchor="nw", fill="x")


		self.text = Label(self.window, wraplength=self.wraplength-50, text="", fg="black")
		self.text.pack(side=TOP, pady=50)

		self.time_text_frame = Frame(self.window)
		self.start = Label(self.time_text_frame, text="Start Time", fg="white")
		self.end = Label(self.time_text_frame, text="End Time", fg="white")

		self.time_text_frame.pack()
		self.start.pack(side=LEFT, padx=40)
		self.end.pack(side=LEFT, padx=80)

		self.wizard_button_frame = Frame(self.window, background="", width=25)
		self.wizard_button_frame.pack(side=BOTTOM, padx=50, pady=50, ipadx=20, anchor="e")

		self.entry_field = Entry(self.window)

		self.cancel = Button(self.wizard_button_frame, text="Cancel", command=lambda: [self.destroy_everything()])
		self.next = Button(self.wizard_button_frame, text="Next")
		self.back = Button(self.wizard_button_frame, text="Back")
		#self.back.pack(side=LEFT, ipadx=5, ipady=5)
		self.next.pack(side=LEFT, ipadx=5, ipady=5)
		self.cancel.pack(side=RIGHT, ipadx=5, ipady=5)

		self.wizard_page1()

	def destroy_everything(self):
		self.cancel.destroy()
		self.next.destroy()
		self.back.destroy()

		self.entry_field.destroy()
		
		self.wizard_button_frame.destroy()
		self.text.destroy()
		self.wizard_header.destroy()
		self.window.destroy()

	def wizard_page1(self):
		self.text.config(text="This wizard will guide you through the creation of your schedule.\nClick \"Next\" to continue, or \"Cancel\" to close the wizard.")
		self.back.config(state=DISABLED)
		self.next.config(command=lambda: [self.wizard_page2()])
		# self.entry_field = Entry(self.window, text="Enter a number here.")
		# self.entry_field.pack(side=TOP)


	def wizard_page2(self):
		self.wizard_header.config(text=" Create Schedule Wizard (Step 1)")
		self.text.config(text="How many classes are you adding?  Enter this number below.")
		self.entry_field.pack(side=TOP)
		self.back.config(state=NORMAL, command=lambda: [self.entry_field.delete(0, END), self.entry_field.pack_forget(), self.wizard_page1()])
		self.next.config(command=lambda: [self.page2_eval_result(self.entry_field.get())])

	def page2_eval_result(self, value):
		try:
			value = int(value)
		except ValueError:
			messagebox.showinfo("Error", "You must enter an integer.")
		else:
			if value > 0:
				self.entry_field.delete(0, END)
				self.entry_field.pack_forget()
				self.wizard_page3(value)
			else:
				messagebox.showinfo("Error", "You must be enrolled in at least 1 class.")


	# 	self.next.config(command=lambda: [wizard_win.destroy()])
	# 	self.cancel.config(command=lambda: self.wizard_page3(wizard_win))
	def wizard_page3(self, input):
		self.entry_field.delete(0, END)
		self.entry_field.pack_forget()
		self.wizard_header.config(text=" Create Schedule Wizard (Step 2)")
		self.text.config(text="Enter the course numbers below.\nThe format for a course number is the department initial(s), followed by the number and a letter, if applicable (e.g., CS313E).")

		course_fields = self.create_course_entry_fields(input)
		self.load_course_fields(course_fields)
		self.back.config(command=lambda: [self.destroy_course_entry_fields(course_fields), self.wizard_page2()])
		self.next.config(command=lambda: self.page3_eval_result(course_fields))

	def page3_eval_result(self, courses):

		# check if they did not enter a result before proceeding (user must have input something)
		for i in range(len(courses)):
			sublist = courses[i]
			if ( len(sublist[1].get()) == 0 ):
				messagebox.showinfo("Error", "You did not enter a course for " + sublist[0].cget("text").replace(':', '') + ".")
				return

		#self.wizard_page4(courses)

	def wizard_page4(self, courses):
		self.wizard_header.config(text=" Create Schedule Wizard (Step 3)")
		self.text.config(text="Enter the start and end. times for each course (in the 12-hour format, e.g. 3:30pm or 12:00pm).")
		self.start.config(fg="black")
		self.end.config(fg="black")
		self.load_endtimes(courses)
		#self.back.config(command=lambda: [self.destroy_endtimes(courses, end_times), self.wizard_page3()])

	def load_endtimes(self, courses):

		for j in range(len(courses)):
			sublist = courses[j]
			end_time = Entry(sublist[2])
			end_time.pack(side=RIGHT)
			sublist[0].config(text=sublist[1].get())
			sublist[1].delete(0, END)
			courses.append(end_time)


	def destroy_course_entry_fields(self, list):
		for i in range(len(list)):
			sublist = list[i]
			for j in range(len(list)):
				sublist[j].destroy()

	def load_course_fields(self, list):
		for i in range(len(list)):
			sublist = list[i]
			sublist[0].pack(side=LEFT)
			sublist[1].pack(side=LEFT)
			sublist[2].pack(side=TOP)

	def create_course_entry_fields(self, num_classes):
		fields = []

		for i in range(num_classes):
			sublist = []
			frame = Frame(self.window, background="")
			label = Label(frame, text="Course " + str(i+1), justify=LEFT)
			entry = Entry(frame)

			sublist.append(label)
			sublist.append(entry)
			sublist.append(frame)
			fields.append(sublist)

		return fields



	# def wizard_page2(self, wizard_win):
	# 	self.text.config(text="How many classes are you adding?  Enter this number below.")
	# 	self.wizard_header.config(text=" Create Schedule Wizard (Step 1)")
	# 	self.entry_field = Entry(wizard_win, text="Enter a number here.")
	# 	self.entry_field.pack(side=TOP)

	# 	self.next.config(command=lambda: [wizard_win.destroy()])
	# 	self.cancel.config(command=lambda: self.wizard_page3(wizard_win))

	# def wizard_page3(self, wizard_win):
	# 	self.text.config(text="Enter the course numbers below.\nThe format for a course number is the department initial(s), followed by the number and a letter, if applicable (e.g., CS313E).")
	# 	self.wizard_header.config(text=" Create Schedule Wizard (Step 3)")

	# 	self.next.config(command=lambda: [wizard_win.destroy()])
	# 	self.cancel.config(command=lambda: self.wizard_page4(wizard_win))

	# 	try:
	# 		self.num_classes = int(self.entry_field.get())
	# 	except ValueError:
	# 		print("egg")
	# 		#messagebox.info("You must enter an integer for the number of classes.")
	# 	else:	
	# 		self.entry_field.delete(0, END)
	# 		self.entry_field.destroy()

	# 		self.frames =[]
	# 		self.labels = []
	# 		self.entries = []

	# 		for i in range(self.num_classes):
	# 			frame = Frame(wizard_win, background="")
	# 			self.frames.append(frame)
	# 			frame.pack(side=TOP)

	# 			label = Label(frame, text="Course " + str(i+1) + ":" )
	# 			self.labels.append(label)
	# 			label.pack(side=LEFT)
	# 			entry = Entry(frame)
	# 			self.entries.append(entry)
	# 			entry.pack(side=TOP)

	# def wizard_page4(self, wizard_win):
	# 	self.text.config(text="What time does each class start and end?  Enter them below.")
	# 	self.wizard_header.config(text=" Create Schedule Wizard (Step 4)")

	# 	table_frame = Frame(wizard_win, background="")
	# 	table_frame.pack(side=TOP)

	# 	start_label = Label(table_frame, text="Start")
	# 	end_label = Label(table_frame, text="End")
	# 	start_label.pack(side=LEFT, padx=15)
	# 	end_label.pack(side=RIGHT, padx=30)

	# 	self.next.config(command=lambda: [wizard_win.destroy()])
	# 	self.cancel.config(command=lambda: [self.wizard_page5(wizard_win), start_label.destroy(), end_label.destroy(), table_frame.destroy()])

	# 	self.inputs = []

	# 	for i in range(len(self.entries)):
	# 		self.labels[i].destroy()
	# 		self.inputs.append(str(self.entries[i].get()))
	# 		print(self.inputs[i])
	# 		self.entries[i].destroy()
	# 		self.frames[i].destroy()

	# 	print(self.inputs)

	# 	self.frames =[]
	# 	self.labels = []
	# 	self.entries = []

	# 	for j in range(len(self.inputs)):
	# 		#print(str(self.inputs[j].get()))
	# 		frame = Frame(wizard_win, background="")
	# 		self.frames.append(frame)
	# 		frame.pack(side=TOP)
	# 		label = Label(frame, text=str(self.inputs[j]) + ":" )
	# 		self.labels.append(label)
	# 		label.pack(side=LEFT)
	# 		start_time = Entry(frame, width=20)
	# 		start_time.pack(side=LEFT)
	# 		end_time = Entry(frame, width=20)
	# 		end_time.pack(side=RIGHT)
	# 		self.entries.append(start_time)
	# 		self.entries.append(end_time)

	# 	# for j in range(len(self.inputs)):
	# 	# 		print("element ", str(j+1), str(self.inputs[j].get()))

	# def wizard_page5(self, wizard_win):
	# 	for i in range(len(self.num_classes)):
	# 		self.labels[i].destroy()
	# 		self.entries[i].destroy()
	# 		self.frames[i].destroy()

	# 	return None