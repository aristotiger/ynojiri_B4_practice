# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 00:02:28 2026

@author: yoshikazu.nojiri
"""

###############################
# ボタン
###############################
"""
import tkinter as tk

root = tk.Tk()

def button_bushed():
    print("Hello world!")

tk.Button(root, text='push!', command=button_bushed).pack()
root.mainloop()
"""
###############################
# 文字列の表示
###############################
"""
import tkinter as tk

root = tk.Tk()

txt = tk.StringVar()
def button_bushed():
    txt.set("Hello world!")

tk.Button(root, text='push!', command=button_bushed).pack()
tk.Entry(root, textvariable=txt).pack()

root.mainloop()
"""
###############################
# 文字列の入力
###############################
"""
import tkinter as tk

root = tk.Tk()

txt = tk.StringVar()
def button_bushed():
    a = txt.get()
    print( a )

tk.Button(root, text='push!', command=button_bushed).pack()
tk.Entry(root, textvariable=txt ).pack()

root.mainloop()
"""
###############################
# スライダーから値の取得
###############################
"""
import tkinter as tk

root = tk.Tk()

def button_bushed():
    print(s.get())

tk.Button(root, text='push!', command=button_bushed).pack()
s = tk.Scale(root, from_=0, to=100, orient="h")
s.pack()

root.mainloop()
"""
###############################
# チェックボックスから選択された値の取得
###############################
"""
import tkinter as tk

root = tk.Tk()

def button_bushed():
    print("Your selection is", selection.get())

tk.Button(root, text='push!', command=button_bushed).pack()

selection = tk.IntVar()
tk.Radiobutton(root, text="aaaa", variable=selection, value=0).pack()
tk.Radiobutton(root, text="bbbb", variable=selection, value=1).pack()

root.mainloop()
"""
###############################
# リストボックスから選択された値の取得
###############################
import tkinter as tk

root = tk.Tk()

def button_bushed():
    i = lb.curselection()[0]
    print("Your selection is", selection[i])

tk.Button(root, text='push!', command=button_bushed).pack()

lb = tk.Listbox(root)
lb.pack()

selection = ["aaa", "bbb", "ccc"]
for s in selection:
    lb.insert(-1, s)

root.mainloop()

