from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
import time
global stz
stz = 0
global sty
sty = 0
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()


def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


def chn(value):
    global stp
    global stz
    if value == "Angle":
        stp = 0
    if value == "Path":
        stp = 1
        stz = 1


def rese():
    global stp
    if stp == 0:
        angle_1_val.delete(0, 10)
        angle_2_val.delete(0, 10)
        angle_3_val.delete(0, 10)
    if stp == 1:
        w.delete("ci")
        w.delete("ci2")


# <!===================================================================================>


def itera():
    global stp
    global st
    st = 1
    if stp == 0:
        print("Angle")
        fileangle = open("angle.txt", "w")
        # print("angle.txt")
        fileangle.write("%s,%s,%s" % (angle_1_val.get(),
                                      angle_2_val.get(), angle_3_val.get()))
        fileangle.close()
    if stp == 1:
        print("Path")
        file2 = open("iteration.txt", "w")
        file3 = open("coordinatesarray.txt", "w")
        file2.write(itr_val.get())
        final_list = []
        for num in selected_points:
            if num not in final_list:
                final_list.append(num)
        file3.write(str(final_list))
        file2.close()
        file3.close()

# <!===================================================================================>


def sending():
    messagebox.showinfo("Message", "File Sent!")


def knobread():
    global sty
    global stz
    if(stz == 1):
        sty = 1
    if(stp == 0):
        GAIN = 1

    print('Reading ADS1x15 values, press Ctrl-C to quit...')
    # Print nice channel column headers.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
    print('-' * 37)

    # Main loop.
    global st
    st = 0
    while (st == 0):
        # Read all the ADC channel values in a list.
        values = [0]*4
        for i in range(4):
            # Read the specified ADC channel using the previously set gain value.
            values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also passas in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        # values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    # print(values[0])
            angle_1_val.delete(0, last=100)
            angle_1_val.insert(0, values[0])
            angle_2_val.delete(0, last=100)
            angle_2_val.insert(0, values[1])
            angle_3_val.delete(0, last=100)
            angle_3_val.insert(0, values[2])
            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # print(values[0]/100)
    # Pause for half a second.
            time.sleep(1)
            root.update()


root = Tk()
root.title('Robotic Arm Controller')
# root.iconbitmap('orangewood.ico')

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
variable = StringVar(content)
variable.set("Select")  # default value


redbutton = Button(content, text='stop', fg='red', command=itera)
greenbutton = Button(content, text='start', fg='green', command=knobread)

resetbut = Button(content, text='Reset', fg='red',
                  command=rese)  # ,command=itera)
sendbut = Button(content, text='Send', fg='red', command=sending)

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
frame.grid(column=2, row=0, columnspan=3, rowspan=14, sticky=(N, S, E, W))
angle_1.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
angle_1_val.grid(column=0, row=1, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)

angle_2.grid(column=0, row=2, columnspan=2, sticky=(N, W), padx=5)
angle_2_val.grid(column=0, row=3, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)


angle_3.grid(column=0, row=4, columnspan=2, sticky=(N, W), padx=5)
angle_3_val.grid(column=0, row=5, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)

Iteration.grid(column=0, row=7, columnspan=2, sticky=(N, W), padx=5)
itr_val.grid(column=0, row=8, columnspan=2,
             sticky=(N, E, W), pady=5, padx=10)


w.grid(column=2, row=0, columnspan=3, rowspan=6)
greenbutton.grid(column=0, row=9, columnspan=2,
                 sticky=(N, E, W), pady=5, padx=10)
redbutton.grid(column=0, row=10, columnspan=2,
               sticky=(N, E, W),  pady=5, padx=10)
resetbut.grid(column=0, row=11, columnspan=2,
              sticky=(N, E, W),  pady=5, padx=10)
sendbut.grid(column=0, row=12, columnspan=2,
             sticky=(N, E, W),  pady=5, padx=10)

option = OptionMenu(content, variable, "Angle", "Path", command=chn)
option.grid(column=0, row=6, columnspan=2,
            sticky=(N, E, W), pady=5, padx=10)


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
content.rowconfigure(9, weight=0)
content.rowconfigure(10, weight=1)

checkered(w, line_distance)
selected_points = []


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def circle(canvas, x, y, r1, r2):
    id = canvas.create_oval(
        x-r1, y-r1, x+r1, y+r1, fill="green", tags="ci")
    id2 = canvas.create_oval(
        x-r2, y-r2, x+r2, y+r2, tags="ci2")
    # return id


def click(event):
    global sty
    if sty == 0:
        messagebox.showinfo("Error", "Can proceed for pathing now!")
    if sty == 1:
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

        # if selected_cordinate not in selected_points :
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
