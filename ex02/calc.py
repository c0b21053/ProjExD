import tkinter as tk
import tkinter.messagebox as tkm

from numpy import column_stack

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    entry.insert(tk.END,txt)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=("",40), justify="right")
entry.grid(row=0,column=0,columnspan=3)

r,c  = 1, 0
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
