from tkinter import *
from tkinter import ttk
import math


def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


root = Tk()
root.title('Robotic Arm Controller')
root.iconbitmap('orangewood.ico')


content = ttk.Frame(root, borderwidth=1)
frame = ttk.Frame(content, borderwidth=1,
                  relief="raised", width=200, height=100)


angle_1 = ttk.Label(content, text="Angle 1", font="Times  14  ")
angle_1_val = ttk.Entry(content)

angle_2 = ttk.Label(content, text="Angle 2", font="Times  14  ")
angle_2_val = ttk.Entry(content)

angle_3 = ttk.Label(content, text="Angle 3",
                    font="Times  14 ")
angle_3_val = ttk.Entry(content)

Iteration = ttk.Label(content, text="Iteration",
                      font="Times  14 ")
itr_val = Spinbox(content, from_=0, to=10)


redbutton = Button(content, text='stop', fg='red')
greenbutton = Button(content, text='start', fg='green')

print(frame.winfo_screenwidth())
print(frame.winfo_screenheight())
line_distance = 100


canvas_width = (math.ceil((frame.winfo_screenwidth()) /
                          line_distance))*line_distance
canvas_height = (math.ceil((frame.winfo_screenheight()) /
                           line_distance))*line_distance

w = Canvas(frame,
           width=canvas_width,
           height=canvas_height)

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=2, row=0, columnspan=3, rowspan=10, sticky=(N, S, E, W))
angle_1.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
angle_1_val.grid(column=0, row=1, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)

angle_2.grid(column=0, row=2, columnspan=2, sticky=(N, W), padx=5)
angle_2_val.grid(column=0, row=3, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)


angle_3.grid(column=0, row=4, columnspan=2, sticky=(N, W), padx=5)
angle_3_val.grid(column=0, row=5, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)

Iteration.grid(column=0, row=6, columnspan=2, sticky=(N, W), padx=5)
itr_val.grid(column=0, row=7, columnspan=2,
             sticky=(N, E, W), pady=5, padx=10)


w.grid(column=2, row=0, columnspan=3, rowspan=6)
greenbutton.grid(column=0, row=8, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)
redbutton.grid(column=0, row=9, columnspan=2,
               sticky=(N, E, W),  pady=5, padx=10)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.rowconfigure(1, weight=0)
content.rowconfigure(2, weight=0)
content.rowconfigure(3, weight=0)
content.rowconfigure(4, weight=0)
content.rowconfigure(5, weight=0)
content.rowconfigure(6, weight=0)
content.rowconfigure(7, weight=0)
content.rowconfigure(8, weight=0)
content.rowconfigure(9, weight=1)


checkered(w, line_distance)
selected_points = []


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def circle(canvas, x, y, r1, r2):
    id = canvas.create_oval(
        x-r1, y-r1, x+r1, y+r1, fill="green")
    id2 = canvas.create_oval(
        x-r2, y-r2, x+r2, y+r2)
    # return id


def click(event):
    x, y = event.x, abs(event.y-canvas_height)
    x_min = (math.floor(x/line_distance))*line_distance
    x_max = (math.ceil(x/line_distance))*line_distance
    y_min = (math.floor(y/line_distance))*line_distance
    y_max = (math.ceil(y/line_distance))*line_distance
    n = [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)]
    dis = []
    # print(n)
    for j in n:
        d = distance((x, y), j)
        dis.append(d)

    print('{}, {}'.format(x, y))
    # print(dis)

    selected_cordinate = n[dis.index(min(dis))]
    selected_points.append(selected_cordinate)
    (x0, y0) = selected_cordinate
    print(selected_points)
    circle(w, x0, canvas_height-y0, 25, 50)


def key(event):
    print("pressed", repr(event.char))


w.bind("<Key>", key)
w.bind("<Button-1>", click)


# root.bind('<Button-1>', click)

root.mainloop()


# csfadfsdgdsfgsdfgz
