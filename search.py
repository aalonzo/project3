try:
    from Tkinter import * 
    #Entry, Frame, Label, StringVar
    from Tkconstants import *
except ImportError:
    from tkinter import *
    from tkinter.constants import *

from PIL import ImageTk, Image
from professor import *
import sys
import os.path
import turtle


INSTALL_DIR = os.getcwd() + "/"


# this method creats the list for the user input or querry
# it also returns an error if the user input is wrong.
def convert(str_rgb):
    try:
        
        rgb = str_rgb[1:]

        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color."% str_rgb)

    return tuple(int(v, 16) for v in (r, g, b))


# This class establishes a default in the search bar when nothing is typed
class Default_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'contains_placeholder'

# This method allows for a default search bar
def add_placeholder(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    # State sets the default search bar for the search.
    state = Default_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.contains_placeholder=True


    def on_focus_in(event, entry=entry, state=state):
        if state.contains_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)
        
            state.contains_placeholder = False

    def on_focus_out(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.contains_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focus_in, add="+")
    entry.bind('<FocusOut>', on_focus_out, add="+")
    
    entry.placeholder_state = state

    return state


# A search bar class
class Search_Bar(Frame):

    # An initializer
    def __init__(self, master, entry_width=30, entry_font=None, entry_background="white", entry_highlightthickness=1, button_text="Search", button_ipadx=10, button_background="#ffffff", button_foreground="black", button_font=None, opacity=0.8, placeholder=None, placeholder_font=None, placeholder_color="grey", spacing=3, command=None):
        Frame.__init__(self, master)
        
        self._command = command

        self.entry = Entry(self, width=entry_width, background=entry_background, highlightcolor=button_background, highlightthickness=entry_highlightthickness)
        self.entry.pack(side=LEFT, fill=BOTH, ipady=1, padx=(0,spacing))
        
        if entry_font:
            self.entry.configure(font=entry_font)

        if placeholder:
            add_placeholder(self.entry, placeholder, color=placeholder_color, font=placeholder_font)

        self.entry.bind("<Escape>", lambda event: self.entry.nametowidget(".").focus())
        self.entry.bind("<Return>", self._on_execute_command)

        opacity = float(opacity)

        if button_background.startswith("#"):
            r,g,b = convert(button_background)
        else:
            r,g,b = master.winfo_rgb(button_background)

        r = int(opacity*r)
        g = int(opacity*g)
        b = int(opacity*b)
        
        if r <= 255 and g <= 255 and b <=255:
            self._button_activebackground = '#%02x%02x%02x' % (r,g,b)
        else:
            self._button_activebackground = '#%04x%04x%04x' % (r,g,b)

        self._button_background = button_background

        self.button_label = Label(self, text=button_text, background=button_background, foreground=button_foreground, font=button_font)
        if entry_font:
            self.button_label.configure(font=button_font)
            
        self.button_label.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
        
        self.button_label.bind("<Enter>", self._state_active)
        self.button_label.bind("<Leave>", self._state_normal)

        self.button_label.bind("<ButtonRelease-1>", self._on_execute_command)

    def get_text(self):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            if entry.placeholder_state.contains_placeholder:
                return ""
            else:
                return entry.get()
        else:
            return entry.get()
        
    def set_text(self, text):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            entry.placeholder_state.contains_placeholder = False

        entry.delete(0, END)
        entry.insert(0, text)
        
    def clear(self):
        self.entry_var.set("")
        
    def focus(self):
        self.entry.focus()

    def _on_execute_command(self, event):
        text = self.get_text()
        self._command(text)

    def _state_normal(self, event):
        self.button_label.configure(background=self._button_background)

    def _state_active(self, event):
        self.button_label.configure(background=self._button_activebackground)
    

if __name__ == "__main__":
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
        from tkinter import Tk
        from tkinter.messagebox import showinfo
        from tkinter import messagebox

    def command(text):
        valid = True
        test_text = text.lower()
        for char in text: # test the inputted text, text should only contain alphabetical char or space
            if char not in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "):
                valid = False
                break
        if test_text == '':
            valid = False
        if valid:
            new_window = Toplevel(root)
            new_window.geometry("800x600")
            new_window.title("Results for \"" + text + "\"")
            img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + "results.png").resize((800, 600), Image.ANTIALIAS))
            bground = Label(new_window, image = img, background="#bf5700")

            bground.place(relx=0.5, rely=0.5, anchor=CENTER)
            Search_Bar(new_window, command=command, placeholder="Search for professors...", entry_highlightthickness=0).pack(side=TOP, anchor="ne", pady=40, padx=50)

            button_frame = Frame(new_window, height=2, bd=5, relief=FLAT)
            button_frame.pack(side=TOP, anchor="nw", pady=10)
            no_result = Label(new_window, text="", fg="black")
            no_result.pack(in_=button_frame, anchor=CENTER)
            
        
            #showinfo("search command", "searching:%s\nDifficulty: %s\nRating: %s"%text%str(query.getDifficulty())%str(query.getRating()))
            #showinfo("search command", "searching: " + text + "\nRating: " + query.getRating() + "\n" + "Difficulty: " + query.getDifficulty() + "\ncomments: " + str(query.getReviews()))
            results = professor_search(text)
            print(len(results))
            if ( len(results) == 0 ):
                no_result.config(text="No results found for \"" + text + "\"", fg="black")
            else:
                for i in range(len(results)):
                    print(results[i].getName())
                    Button(new_window, text=results[i].getName() + ", Difficulty: " + str(results[i].getDifficulty()) + ", Rating: " + str(results[i].getRating()), padx=5, pady=5, command=lambda i=i: display_comment(results[i])).pack(side=TOP, anchor="nw")
                no_result.config(text=str(len(results)) + " result(s) found.")
                no_result.update()

            new_window.mainloop()

        elif not valid and text == "":
            messagebox.showerror("Empty Search", "Search bar cannot be left blank.")
            raise Exception("Empty Search Error")
        else:
            messagebox.showerror("Invalid Text Entry", "Search term cannot contain numerical characters or \
symbols. Please enter text containing only alphabetical characters and spaces.")
            raise Exception("Invalid Text Error")
            
    
    # def update_scene(root, milsec, filename):
    #     self.img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + filename))
    #     #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    #     self.master.after(milsec, self.panel.config(image = self.img))
    #     self.master.update()
    def display_comment(result):
        res_window = Toplevel(root)
        res_window.geometry("800x600")
        res_window.title("Comments about " + result.getName())
        header = Label(res_window, text="Comments From Others", font=('Arial', 36), bg="#bf5700", fg="white", justify=LEFT)
        header.pack(side=TOP, anchor="nw", fill="x")
        reviews = result.getReviews()
        print(reviews)
        scrollbar = Scrollbar(res_window)
        scrollbar.pack(side=RIGHT, fill=Y)
        comment_box = Text(res_window, wrap=WORD, yscrollcommand=scrollbar.set)
        for i in range(len(reviews)):
            comment_box.insert(END, str(i+1) + ". " + reviews[i] + "\n\n")
        comment_box.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=comment_box.yview)
        res_window.mainloop()

    root = Tk()
    root.geometry("800x600")
    root.title("Search")
    root.config(background="#bf5700")

    img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + "home.png").resize((800, 600), Image.ANTIALIAS))
    # img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + "home.png"))
    panel = Label(root, image = img, background="#bf5700")


    panel.place(relx=0.5, rely=0.5, anchor=CENTER)
    Search_Bar(root, command= command, placeholder="Search for professors...", entry_highlightthickness=0).pack(side=BOTTOM, pady=130, padx=3)
    root.mainloop()
