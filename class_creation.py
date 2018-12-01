from tkinter import *
from tkinter import messagebox

class course:
    def __init__(self):
        self.name = ""
        self.days = [False, False, False, False, False] # Mon, Tue, Wed, Thur, Fri
        self.times = [[],[],[],[],[]]

    # def update_name:
    # def add_time: # will add an additional time to course
    # def update_time: # will change a time that is already present
    # def delete_time: # will remove a time in course

def add(couse_lst, name, mon, tue, wed, thu, fri, t1, ampm1, t2, ampm2):
    if t1 == "" or t2 == "":
        raise Exception("Left Blank Error")
        messagebox.showinfo("Empty Value", "One of the times was left blank. Please \
fill in these values")
    if len(t1) not in (3,4,5) or len(t2) not in (3,4,5):
        raise Exception("Invalid Format Error")
        messagebox.showinfo("Invalid Time Format", "One of the times was incorrectly \
formatted. Please enter the time in a valid format (Ex: 3:00)")
    
    
    if ":" in t1: # will be length 4 or 5 (ex: 3:00 or 12:00)
        if len(t1) == 4:
            t1 = "0" + t1
        if t1[2] == ":": # Assuming length of string is 5
            t1 = t1[0:2] + t1[3:] # include char from 0 up to but not including 2
    elif len(t1) == 3:
        t1 = "0" + t1

    if ":" in t2: # will be length 4 or 5 (ex: 3:00 or 12:00)
        if len(t2) == 4:
            t2 = "0" + t2
        if t2[2] == ":": # Assuming length of string is 5
            t2 = t2[0:2] + t2[3:]
    elif len(t2) == 3:
        t2 = "0" + t2

    # Assuming the values are valid

    classy = course()
    
    classy.name = name
        
    lst_days_val = [mon, tue, wed, thu, fri] # values for check buttons
    lst_days_bool = []
    for i in lst_days_val: # assign true or false values
        if i == 1:
            lst_days_bool += [True]
        else:
            lst_days_bool += [False]

    new_t1 = ""
    for m in t1:
        if m in ('1','2','3','4','5','6','7','8','9','0'):
            new_t1 += m
    new_t2 = ""
    for n in t2:
        if n in ('1','2','3','4','5','6','7','8','9','0'):
            new_t2 += n

    time1 = int(new_t1)
    time2 = int(new_t2)
    if time1 == 1200:
        time1 = 0
    if time2 == 1200:
        time2 = 0
    if ampm1 == 1: # pm was selected
        time1 += 1200
    if ampm2 == 1: # pm was selected
        time2 += 1200
            
    x = 0
    for j in lst_days_bool:
        if j:
            if [time1, time2] not in classy.times[x]:
                classy.times[x].append([time1, time2])
        x += 1
        
    classy.days = lst_days_bool

    print(classy.name)
    print(classy.days)
    print(classy.times)
            
    

def main():

    master = Tk()
    variable = StringVar(master)
    variable.set("one") # default value

    course_lst = []

    check_var0 = IntVar()
    check_var1 = IntVar()
    check_var2 = IntVar()
    check_var3 = IntVar()
    check_var4 = IntVar()
    
    radio_var1 = IntVar()
    radio_var2 = IntVar()

    lab0 = Label(master, text = "Course Number")
    lab0.pack()
    e0 = Entry(master)
    e0.pack()

    cb0 = Checkbutton(master, text = "Monday", variable=check_var0, \
                      onvalue = 1, offvalue = 0)
    cb0.pack()
    cb1 = Checkbutton(master, text = "Tuesday", variable=check_var1, \
                      onvalue = 1, offvalue = 0)
    cb1.pack()
    cb2 = Checkbutton(master, text = "Wednesday", variable=check_var2, \
                      onvalue = 1, offvalue = 0)
    cb2.pack()
    cb3 = Checkbutton(master, text = "Thursday", variable=check_var3, \
                      onvalue = 1, offvalue = 0)
    cb3.pack()
    cb4 = Checkbutton(master, text = "Friday", variable=check_var4, \
                      onvalue = 1, offvalue = 0)
    cb4.pack()

    lab1 = Label(master, text = "Start Time")
    lab1.pack()
    e1 = Entry(master)
    e1.pack()
    rb0 = Radiobutton(master, text = "AM", variable=radio_var1, value=0)
    rb0.pack()
    rb1 = Radiobutton(master, text = "PM", variable=radio_var1, value=1)
    rb1.pack()

    lab2 = Label(master, text = "End Time")
    lab2.pack()
    e2 = Entry(master)
    e2.pack()
    rb2 = Radiobutton(master, text = "AM", variable=radio_var2, value=0)
    rb2.pack()
    rb3 = Radiobutton(master, text = "PM", variable=radio_var2, value=1)
    rb3.pack()

    add_but = Button(master, text = "add class", command = \
                    lambda:add(course_lst, e0.get(), \
                                  check_var0.get(), check_var1.get(), \
                                  check_var2.get(), check_var3.get(), check_var4.get(), \
                                  e1.get(), radio_var1.get(), e2.get(), radio_var2.get()))
    add_but.pack()
    

    master.mainloop()
    

main()
        
