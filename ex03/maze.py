import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_loop():
    global mx, my, g
    global cx, cy
    g = 1
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -=1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx +=1
        if key == "Right":
            mx -= 1
    
    canv.coords("tori", cx, cy)
    root.after(100, main_loop)

    if mx == 13 and my == 7:
        message = tk.Message(root, text = "Congratulation!!",
        font=("",60),bg = "yellow")
        message.place(x=550,y=300,width=400,height=300)

        return    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canv, maze_lst)

    tori = tk.PhotoImage(file = "fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    
    main_loop()
    


    root.mainloop()