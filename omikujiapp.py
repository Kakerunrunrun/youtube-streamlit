import tkinter as tk
import random 

def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶", "大凶"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk
root.geometry("300x130")

lbl = tk.Label(text="Welcome to kuji")
btn = tk.Button(text="PUSH HERE TO DRAW KUJI", command = dispLabel)


lbl.pack()
btn.pack()
tk.mainloop