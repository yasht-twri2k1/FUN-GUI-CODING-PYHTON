from tkinter import *
 
root = Tk()
root.configure(bg="black")
root.geometry('1000x1000')
root.title("+++WELCOME TO CHANNEL+++")
var_lb=Label(root,text="===>>WELCOME TO MY BLOG<===",font=("Times New Roman",45),bg="black",fg="white") 
var_lb.grid(column=1,row=0)

var_lb1=Label(root,text="====++====ARIGATO!===++===",font=("Bold Italic",35),bg="black",fg="white")
var_lb1.grid(column=1,row=2)

var1_lb=Label(root,text="HEY,its me YASH for interesting facts 'subscribe my BLOG Channel'",font=("Bold Italic",21),bg="black",fg="white")
var1_lb.grid(column=1,row=3)

Nam_lbl=Label(root,text="ENTER NAME:",font=("Times New Roman",30),bg="black",fg="white")
Nam_lbl.grid(column=1,row=4)


txt=Entry(root,width=15,font=("Times New Roman",30))
txt.grid(column=1,row=4)
#var_name=txt

'''bg=PhotoImage(file = u"img.jpg")
label1=Label(root,image=bg)
label1.place(x=20,y=0)

label2=Label(root,text="Welcome")
label2.pack(pady=20)

frame1=Frame(root)
frame1.pack(pady=20)'''


def clicked():
    result="WELCOME TO MY BLOG :-\t" + txt.get()
    var_lb1.configure(text=result,font=("Bold Italic",35),bg="black",fg="white")
    var1_lb.configure(text="===>THANkS FOR SUBSCRIBING<===",font=("Times New Roman",35),bg="black",fg="white")
    var1_lb.grid(column=1,row=6)
click_btn=Button(root,text="SUBSCRIBE ME",font=("Times New Roman",35),bg="red",fg="white",command=clicked)
click_btn.grid(column=1,row=5)
root.mainloop()



