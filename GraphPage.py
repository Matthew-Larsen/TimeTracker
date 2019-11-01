import tkinter as tk
from tkinter import ttk

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import GrapherController as gc


# class GraphPage():
#
#     def __init__(self, master):
#         #tk.Frame.__init__(self, master)
#
#         #label = tk.Label(self, text="Graph Page!", font)
#
#         self.label = tk.Label(master, text="This is graph page.")
#         self.label.pack()
#
#         self.master = master
#         master.title("Graph Page")
#
#
#         f = Figure(figsize=(5,5), dpi =100)
#         a = f.add_subplot(111)
#         a.plot([1, 2,3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 6, 7, 3, 0])
#
#         canvas = FigureCanvasTkAgg(f, master)
#         canvas.draw()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH, expand=True)
#
#
#
#
#         #self.startButton = tk.Button(master, text="Start", command=self.start)
#         #self.startButton.grid(row=1)
#
#         #self.closeButton = tk.Button(master, text="Close", command=master.quit)
#         #self.closeButton.grid(row=1, column=1)
#
#
#
#     def start(self):
#         print("Start")
#
# root = tk.Tk()
# myGui = GraphPage(root)
# root.mainloop()


class TimeGrapher(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Time Grapher")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, Graph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nesw")
        self.show_frame(StartPage)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=("Verdana", 12))
        label.pack()
        button = ttk.Button(self, text="Begin Graphing", command=lambda: controller.show_frame(Graph))
        button.pack()


class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=("Verdana", 12))
        label.pack(padx=10, pady=10)

        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)

        gc.forceLoad()
        plot_data(a, gc.get_data())

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


def plot_data(subplot, data):
    names = []
    sizes = []
    for task in data.tasks:
        name = task.name
        if len(name) > 10:
            namebits = name.split(" ")
            name = ""
            for bit in namebits:
                name += bit + "\n"
        names.append(name)
        size = 0
        for use in task.usage_data:
            size += use.elapsed_time.total_seconds()
        sizes.append(size)
    subplot.pie(sizes, labels=names, autopct='%.1f%%', frame=False, rotatelabels=True)
    subplot.axis('equal')


app = TimeGrapher()
app.mainloop()
