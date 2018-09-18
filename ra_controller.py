from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth=5,
                  relief="sunken", width=200, height=100)
angle_1 = ttk.Label(content, text="Angle 1", font="Times  14  ")
angle_1_val = ttk.Entry(content)

angle_2 = ttk.Label(content, text="Angle 2", font="Times  14  ")
angle_2_val = ttk.Entry(content)

angle_3 = ttk.Label(content, text="Angle 3",
                    font="Times  14 ")
angle_3_val = ttk.Entry(content)

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=2, row=0, columnspan=3, rowspan=6, sticky=(N, S, E, W))
angle_1.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
angle_1_val.grid(column=0, row=1, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)

angle_2.grid(column=0, row=2, columnspan=2, sticky=(N, W), padx=5)
angle_2_val.grid(column=0, row=3, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)


angle_3.grid(column=0, row=4, columnspan=2, sticky=(N, W), padx=5)
angle_3_val.grid(column=0, row=5, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=0)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=0)
content.rowconfigure(5, weight=1)


root.mainloop()
