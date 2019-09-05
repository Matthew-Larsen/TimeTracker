import tkinter as tk

import GrapherController as controller

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

root.mainloop()

def init_gui():
    loading_label = tk.Label(frame, text="Loading")
    loading_label.pack()
    frame.update()



def show_no_data():
    clear_root()
    no_data_label = tk.Label(frame, text="There is no time data to display.\n Click below to " +
                                         "start the time tracker on startup")
    no_data_label.pack()
    begin_on_startup_button = tk.Button(frame, text="Add to startup")
    begin_on_startup_button.bind("<Button-1>", controller.button_pressed)
    begin_on_startup_button.pack()

    frame.update()


def show_data(task_list):
    clear_root()
    data_label = tk.Label(frame, text="Success?")
    data_label.pack()


def clear_root():
    global frame
    frame.destroy()
    frame = tk.Frame(root)
