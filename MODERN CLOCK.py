from tkinter import Label, Tk 
import time
window = Tk() 
window.title("MODERN Clock") 
window.geometry("420x150") 
window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "black"
foreground= "red"
border_width = 25

label = Label(window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def modern_clock(): 
   current_time = time.strftime("%H:%M:%S")
   label.config(text=current_time) 
   label.after(300,  modern_clock)

modern_clock()
app_window.mainloop()
