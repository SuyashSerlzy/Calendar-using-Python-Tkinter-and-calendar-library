from tkinter import* #this will import tkinter and calendar library
import calendar
root= Tk()
calendar = calendar.calendar(2022)
root.title("Calendar")
root.configure(bg = '#000000')
root.geometry('400x500')
root.resizable(False, False)
label1 = Label(root, text = "CALENDAR", bg = '#000', fg = '#FFFFFF').place(x = 180, y = 20)
label2 = Label(root, text = calendar, bg = '#000', fg = 'white', font = "consoles 7 bold").place(x = 30, y = 50)
root.mainloop()
