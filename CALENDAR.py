#Importing tkinter module
from tkinter import *
#importing calendar module
import calendar

#function to show calendar of the given year
def showCalender():
    root= Tk()
    root.config(background='red')
    root.title("Calender for the year")
    root.geometry("600x700")
    year = int(year_field.get())
    root_content= calendar.calendar(year)
    calYear = Label(root, text= root_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    root.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='black')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calander",bg='red',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='grey')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='Black',bg='light green',command=showCalender)

    #putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    #Exit.grid(row=6, column=1)
    new.mainloop()
