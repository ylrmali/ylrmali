from tkinter import *

window = Tk()

def button_click(number):
    entry.delete(0, END)
    current = entry.get()
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "toplama"
    f_num = int(first_number)
    entry.delete(0,END)

def button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    
    if math=="toplama":
        entry.insert(0, f_num + int(second_number))
    if math=="cıkarma":
        entry.insert(0, f_num - int(second_number))
    if math=="carpma":
        entry.insert(0, f_num * int(second_number))
    if math=="bolme":
        entry.insert(0, f_num / int(second_number))
    

def button_subtract():
	first_number = entry.get()
	global f_num
	global math
	math = "cıkarma"
	f_num = int(first_number)
	entry.delete(0, END)

def button_multiply():
	first_number = entry.get()
	global f_num
	global math
	math = "carpma"
	f_num = int(first_number)
	entry.delete(0, END)

def button_divide():
	first_number = entry.get()
	global f_num
	global math
	math = "bolme"
	f_num = int(first_number)
	entry.delete(0, END)


window.resizable(height=False ,width=False )
window.title("Hesap Makinası")
window.config(bg="black")
window.configure(bg="black")
window.geometry("300x325")


entry = Entry(window , width=100 , bg="light grey",borderwidth=0 , font=("normal", 40) )
entry.place(x=0 , y =0 , height=100 , width=300) 


button0 = Button(window)
button0.config(text="0", bg="#ffc637", fg="black",width=8,height=3 ,command=lambda: button_click(0))
button0.place(x=0,y=268)

button1 = Button(window)
button1.config(text="1", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(1))
button1.place(x=0 , y=212)

button3 = Button(window)
button3.config(text="3", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(3))
button3.place(x=132 , y=212)

button2 = Button(window)
button2.config(text="2", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(2))
button2.place(x=66 , y=212)

button4 = Button(window)
button4.config(text="4", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(4))
button4.place(x=0 , y=156)

button5 = Button(window)
button5.config(text="5", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(5))
button5.place(x=66, y=156)

button7 = Button(window)
button7.config(text="7", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(7))
button7.place(x=0 , y=100)

button8 = Button(window)
button8.config(text="8", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(8))
button8.place(x=66 , y=100)

button9 = Button(window)
button9.config(text="9", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(9))
button9.place(x=132 , y=100)

button_eksi = Button(window)
button_eksi.config(text="-", bg="#ffc637", fg="black",width=13 ,height=3,command= button_subtract)
button_eksi.place(x=198 , y=100)

button6 = Button(window)
button6.config(text="6", bg="#ffc637", fg="black",width=8 ,height=3,command=lambda: button_click(6))
button6.place(x=132, y=156)

button_artı = Button(window)
button_artı.config(text="+", bg="#ffc637", fg="black",width=13 ,height=3,command=button_add)
button_artı.place(x=198, y=156)

button_carpı = Button(window)
button_carpı.config(text="X", bg="#ffc637", fg="black",width=13 ,height=3,command=button_multiply)
button_carpı.place(x=198, y=212)

button_bolu = Button(window)
button_bolu.config(text="/", bg="#ffc637", fg="black",width=13 ,height=3,command=button_divide)
button_bolu.place(x=198, y=268)

button_esit = Button(window)
button_esit.config(text="=", bg="#ffc637", fg="black",width=8 ,height=3,command=button_equal)
button_esit.place(x=66 , y=268)

button_c = Button(window)
button_c.config(text="Clear", bg="#ffc637", fg="black",width=8 ,height=3, command=button_clear)
button_c.place(x=132 , y=268)

mainloop()
