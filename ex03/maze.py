import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_loop():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -=20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_loop)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    tori = tk.PhotoImage(file = "fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_loop()

    maze_lst = mm.make_maze(15, 9)
    

    root.mainloop()