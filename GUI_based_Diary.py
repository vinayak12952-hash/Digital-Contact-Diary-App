# importing Modules
import tkinter as tk
from Digital_Diary_by_json import ContactBook as diary

# making Home screen
Diary_Scr = tk.Tk()

# defining title and size
Diary_Scr.title("Contact Book")
Diary_Scr.geometry("500x250")

# defiing heading
heading = tk.Label(Diary_Scr, text="Welcome to your Contact Book!")

# taking name for the formation of file
user_name_text= tk.Label(Diary_Scr, text="Enter your name: ")
user_name_entry= tk.Entry(Diary_Scr)

# making function for appearing save window
def add_save_window():
    save_window = tk.Toplevel(Diary_Scr)
    save_window.geometry("300x150")
    name_text= tk.Label(save_window, text="Enter person's name: ")
    name_entry= tk.Entry(save_window)

    number_text= tk.Label(save_window, text="Enter the number of the person:")
    number_entry= tk.Entry(save_window)

    output = tk.Label(save_window,text= "Nothing")

    # making save function.
    def save():
        user_name = user_name_entry.get()
        name = name_entry.get()
        number = number_entry.get()
    
        object = diary(user_name)
        object.add(name, number)

        output.config(text="Entry saved")
        output.pack()
        

    save_contact_button = tk.Button(save_window,text="Save", command= save)

    name_text.pack()
    name_entry.pack()
    number_text.pack()
    number_entry.pack()
    save_contact_button.pack()

# making function for appearing find window.
def add_find_window():
    find_window = tk.Toplevel(Diary_Scr)
    find_window.geometry("300x150")
    name_text= tk.Label(find_window, text="Enter person's name: ")
    name_entry= tk.Entry(find_window)

    output = tk.Label(find_window,text= "Nothing")

    # making find function 
    def find():
        user_name = user_name_entry.get()
        name = name_entry.get()

        object = diary(user_name)
        object.search(name)
        result = object.search(name)
        
        output.config(text=result)
        output.pack()
    
    find_contact_button = tk.Button(find_window,text="Find", command=find)

    name_text.pack()
    name_entry.pack()
    find_contact_button.pack()

save_button = tk.Button(Diary_Scr, text="To save contact", command=add_save_window )
find_button = tk.Button(Diary_Scr, text="To find contact", command=add_find_window )

heading.place(x=170, y= 30)
user_name_text.place(x=170 , y= 80)
user_name_entry.place(x=170 , y=100 )
save_button.place(x = 50, y = 150)
find_button.place(x = 350 , y = 150)

Diary_Scr.mainloop()