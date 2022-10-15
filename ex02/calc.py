import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")

root = tk.Tk()
root.geometry("300x500")

r,c  = 0, 0
for i,num in enumerate(range(9,-1,-1),1):
    button = tk.Button(root,text=num,font=("",30), width=4, height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    if i%3==0:
        r += 1
        c = 0
    else:
        c+=1


root.mainloop()
