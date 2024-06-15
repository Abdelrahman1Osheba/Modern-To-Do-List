import customtkinter
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import *

def back_to_calendar(app, position, size):
    app.destroy()
    open_calendar_window(position, size)

def open_main_window(selected_date, position, size):
    appl.destroy()
    app = customtkinter.CTk()
    app.title('To Do List')
    app.geometry(f'{size[0]}x{size[1]}+{position[0]}+{position[1]}')
    app.resizable(False, False)
    app.config(bg="#09112e")

    font1 = ('Arial', 30, 'bold')
    font2 = ('Arial', 18, 'bold')
    font3 = ('Arial', 10, 'bold')

    def add_task():
        task = task_entry.get()
        if task:
            task_list.insert(0, task)
            task_entry.delete(0, END)
            save_task()
        else:
            messagebox.showerror("Empty", "Please Enter a Task")

    def remove_task():
        selected_task = task_list.curselection()
        if selected_task:
            task_list.delete(selected_task[0])
            save_task()
        else:
            messagebox.showerror("Not Selected", "Please Choose a Task")

    def save_task():
        filename = f"tasks_{selected_date}.txt"
        with open(filename, "w") as f:
            tasks = task_list.get(0, END)
            for task in tasks:
                f.write(task + "\n")

    def load_tasks():
        filename = f"tasks_{selected_date}.txt"
        try:
            with open(filename, "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    task_list.insert(END, task.strip())
        except FileNotFoundError:
            pass

    title_label = customtkinter.CTkLabel(app, font=font1, text='To-Do List', text_color='#fff', bg_color='#09112e')
    title_label.place(x=130, y=10)

    add_button = customtkinter.CTkButton(
        app, font=font2, text='Add', text_color='#fff',
        fg_color='#008000', hover_color='#008000', bg_color='#09112e', cursor='hand2',
        corner_radius=20, width=150, command=add_task
    )
    add_button.place(x=40, y=100)

    delete_button = customtkinter.CTkButton(
        app, font=font2, text='Delete',
        text_color='#fff', fg_color='#8B0000', hover_color='#8B0000', bg_color='#09112e',
        cursor='hand2', corner_radius=20, width=150, command=remove_task
    )
    delete_button.place(x=230, y=100)

    task_entry = customtkinter.CTkEntry(app, font=font3, text_color='#000', fg_color='#fff', border_color='#09112e', bg_color="#09112e",  width=340)
    task_entry.place(x=40, y=50)

    task_list = Listbox(app, font=font3, height=15, width=60)
    task_list.place(x=50, y=200)


    back_button = customtkinter.CTkButton(
        app, font=font2, text='Back',
        text_color='#fff', fg_color='#1A2A7D', hover_color='#1A2A7D', bg_color='#09112e',
        cursor='hand2', corner_radius=20, width=150, command=lambda: back_to_calendar(app, position, size)
    )
    back_button.place(x=130, y=400)

    load_tasks()
    app.mainloop()

def on_date_select():
    selected_date = cal.selection_get()
    position = (appl.winfo_x(), appl.winfo_y())
    size = (appl.winfo_width(), appl.winfo_height())
    open_main_window(selected_date, position, size)

def open_calendar_window(position, size):
    global appl, cal
    appl = Tk()
    appl.title('Select Date')
    appl.geometry('400x500+100+100')
    appl.resizable(False, False)
    appl.config(bg="#09112e")

    font2 = ('Arial', 18, 'bold')

    cal = Calendar(
        appl, selectmode='day', year=2024, month=6, day=15,
        background='darkblue', foreground='white', selectbackground='lightblue', selectforeground='white'
    )
    cal.place(x=80, y=20)
    select_button = customtkinter.CTkButton(
        appl, font=font2, text='Select Date',
        text_color='#fff', fg_color='#1A2A7D', hover_color='#1A2A7D', bg_color='#09112e',
        cursor='hand2', corner_radius=20, width=150, command=on_date_select
    )
    select_button.place(x=130, y=220)

    appl.mainloop()

position = (100, 100)
size = (400, 500)
open_calendar_window(position, size)
