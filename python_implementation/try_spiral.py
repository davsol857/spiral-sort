import spiral_sort
import tkinter

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

canvas.create_text(500, 15, text="Press 'a' to get spiral")

list_body = list()


def get_spiral(event):
    global list_body
    canvas.destroy()
    canvas.unbind_all("<Button-1>")

    spiral_1 = spiral_sort.spiral_sort(points=list_body,
                                       rotation="right",
                                       visualize=True)
    print(spiral_1.sort())


def klik(event):
    global list_body
    canvas.create_oval(int(event.x)-3, int(event.y)-3,
                       int(event.x)+3, int(event.y)+3,
                       fill="red", width=0)

    list_body.append((int(event.x),
                     int(event.y)))


canvas.bind_all("<Button-1>", klik)
canvas.bind_all("a", get_spiral)
