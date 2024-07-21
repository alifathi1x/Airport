import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Airport")
win.geometry("600x600")
tk.Label(win, text="Customer Information",font="Arial 12 bold").place(x=200,y=30)
tk.Label(win, text="نام",font="Arial 15 bold").place(x=250,y=70)
tk.Entry(win, width=12, font="arial 10 bold",bd=3).place(x=300,y=70)
tk.Label(win, text="نام خانوادگی",font="Arial 15 bold").place(x=230,y=130)
tk.Entry(win, width=12, font="arial 10 bold",bd=3).place(x=340,y=130)
tk.Label(win, text="تاریخ تولد",font="Arial 15 bold").place(x=240,y=200)
tk.Entry(win, width=12, font="arial 10 bold",bd=3).place(x=340,y=200)
tk.Label(win, text="کد ملی",font="Arial 15 bold").place(x=250,y=270)
tk.Entry(win, width=12, font="arial 10 bold",bd=3).place(x=350,y=270)
tk.Label(win, text="شمار پاسپورت",font="Arial 15 bold").place(x=230,y=330)
tk.Entry(win, width=12, font="arial 10 bold",bd=3).place(x=340,y=330)
tk.Button(win, text="save",font="Arial 15 bold",activebackground="white",command="save",background="dark blue").place(x=300,y=500)
tk.Button(win, text="exit",font="Arial 15 bold",activebackground="white",command=exit,background="dark blue").place(x=370,y=500)




win.mainloop()
