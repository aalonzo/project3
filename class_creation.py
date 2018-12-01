from tkinter import *

class classy:
    def __init__(self):
        self.name = ""
        self.days = [False, False, False, False, False] # Mon, Tue, Wed, Thur, Fri
        self.times = [[],[],[],[],[]]
    '''
    def changeDay(self, day):
        day = day.lower()
        if text in ["m", "t", "w", "th", "f"]:
            i = 0
            for j in ["m", "t", "w", "th", "f"]:
                if text == j:
                    break
                elif text < 4:
                    i += 1
            self.days[i] = not self.days[i] # change boolean to opposite
            if not self.days[i]: # was changed to false
                self.times = [[],[],[],[],[]]

    def changeTimes(self, day, time): # day = str and time = list length 2
        if day in ["m", "t", "w", "th", "f"]:
            pass
            '''

def submit(classy, mon, tue, wed, thu, fri):
    #print(str(mon.get()))
    lst_days_val = [mon.get(), tue.get(), wed.get(), thu.get(), fri.get()]
    lst_days_bool = []
    for i in lst_days_val:
        if i == 1:
            lst_days_bool += [True]
        else:
            lst_days_bool += [False]
    print(lst_days_bool)
    classy.days = lst_days_bool
    print(classy.days)
            
    

def main():

    master = Tk()
    variable = StringVar(master)
    variable.set("one") # default value

    class1 = classy()
    current_class = classy()

    check_var0 = IntVar()
    check_var1 = IntVar()
    check_var2 = IntVar()
    check_var3 = IntVar()
    check_var4 = IntVar()
    
    radio_var1 = IntVar()
    radio_var2 = IntVar()

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

    lab0 = Label(master, text = "Start Time")
    lab0.pack()
    e0 = Entry(master)
    e0.pack()
    rb0 = Radiobutton(master, text = "AM", variable=radio_var1, value=0)
    rb0.pack()
    rb1 = Radiobutton(master, text = "PM", variable=radio_var1, value=1)
    rb1.pack()

    lab1 = Label(master, text = "End Time")
    lab1.pack()
    e1 = Entry(master)
    e1.pack()
    rb2 = Radiobutton(master, text = "AM", variable=radio_var2, value=0)
    rb2.pack()
    rb3 = Radiobutton(master, text = "PM", variable=radio_var2, value=1)
    rb3.pack()

    button = Button(master, text = "submit", command = \
                    lambda:submit(current_class, check_var0, check_var1, check_var2, check_var3, check_var4))
    button.pack()

    #print(str(check_var1.get()))

    master.mainloop()
    
    #class1 = classy()
    #class1.changeDay("m")
    #print (class1.days)

main()
        
