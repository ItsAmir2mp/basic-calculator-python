# START
from tkinter import *
import math
# def
def exit():
    window2.destroy()
def btns(character):
    entry_number.insert(END, character)
def C():
    length = len((entry_number.get()))
    entry_number.delete(length-1)
def CE():
    entry_number.delete(0 , END)
def radical():
    answer = math.sqrt(int(entry_number.get()))
    entry_number.delete(0, END)
    entry_number.insert(0,answer)

def show_result():
    try:
        answer = eval(entry_number.get())
        entry_number.delete(0,END)
        entry_number.insert(0, answer)
    except:
        entry_number.delete(0,END)
        entry_number.insert(0,'Error')
def myabs():
    answer = abs(int(entry_number.get()))
    entry_number.delete(0,END)
    entry_number.insert(0,answer)
# window 2
window2 = Tk()
window2.geometry('197x160')
window2.title('')
window2.resizable(0,0)
# labels,button,entry
btn_exit2 = Button(window2 , text='Exit',bg = 'red' , fg='white',command =exit)
btn_exit2.place(x =  0, y = 130 , width=25,height=30)
# cal buttons
button_name1 = Button(window2 , text='C' , bg='black',fg='white' , command=C )
button_name1.grid(row=1 , column=1 , sticky='NWSE')
button_name2 = Button(window2 , text='=' , bg='blue',fg='white', command= show_result)
button_name2.grid(row=1 , column=2 , sticky='WNSE')
button_name3 = Button(window2 , text='-', bg='black',fg='white', command= lambda : btns('-'))
button_name3.grid(row=1 , column=4 ,sticky='WSNE')
button_name4 = Button(window2 , text='+', bg='black',fg='white', command= lambda : btns('+'))
button_name4.grid(row=2 , column=4 ,sticky='WNSE')
button_name5 = Button(window2 , text='%', bg='black',fg='white', command= lambda : btns('%'))
button_name5.grid(row=4 , column=4 , sticky='WSNE')
button_name6 = Button(window2 , text='÷', bg='black',fg='white', command= lambda : btns('/'))
button_name6.grid(row=3 , column=4 , columnspan=10 , sticky='WSNE')
button_name7 = Button(window2 , text='CE', bg='black',fg='white' , command = CE)
button_name7.grid(row=2, column=1 , sticky='W')
button_name8 = Button(window2 , text='7', width=2,height=1, bg='black',fg='white',command= lambda : btns(7))
button_name8.grid(row=3 , column=1 , sticky='W')
button_name9 = Button(window2 , text='8', width=2,height=1, bg='black',fg='white',command= lambda : btns(8))
button_name9.grid(row=3 , column=2 , sticky='WE')
button_name10 = Button(window2 , text='4', width=2,height=1, bg='black',fg='white',command= lambda : btns(4))
button_name10.grid(row=4 , column=1 , sticky='WEN')
button_name11 = Button(window2, text='1', width=2,height=1, bg='black',fg='white', command= lambda : btns(1))
button_name11.grid(row=5 , column=1 , sticky='W')
button_name12 = Button(window2, text='2', width=2,height=1, bg='black',fg='white', command= lambda : btns(2))
button_name12.grid(row=5 , column=2 , sticky='WE')
button_name13 = Button(window2, text='5', width=2,height=1, bg='black',fg='white', command= lambda : btns(5))
button_name13.grid(row=4 , column=2 , sticky='WE')
button_name14 = Button(window2, text='9', width=2,height=1, bg='black',fg='white', command= lambda : btns(9))
button_name14.grid(row=3, column=3 , sticky='W')
button_name15 = Button(window2, text='6', width=2,height=1, bg='black',fg='white', command= lambda : btns(6))
button_name15.grid(row=4 , column=3 , sticky='W')
button_name16 = Button(window2, text='3', width=2,height=1, bg='black',fg='white', command= lambda : btns(3))
button_name16.grid(row=5 , column=3 , sticky='W')
button_name17 = Button(window2, text='0', width=2,height=1, bg='black',fg='white', command= lambda : btns(0))
button_name17.grid(row=2 , column=3 , sticky='W')
button_name18 = Button(window2, text='/', width=2,height=1, bg='black',fg='white', command= lambda : btns('/'))
button_name18.grid(row=1 , column=3 , sticky='W')
button_name19 = Button(window2, text='√',width=2,height=1, bg='black',fg='white' , command =  radical)
button_name19.grid(row=5 , column=4 , sticky='W')
button_name20 = Button(window2, text='X',width=2,height=1, bg='black',fg='white' , command= lambda : btns("*"))
button_name20.place(x= 174 , y=130 ,width=28,height=30)
button_name21 = Button(window2, text='^',width=2,height=1, bg='black',fg='white' , command= lambda : btns("**"))
button_name21.place(x= 150 , y=130 ,width=24,height=30)
button_name22 = Button(window2, text='|X|',width=2,height=1, bg='black',fg='white' , command= myabs)
button_name22.place(x= 25 , y=130 ,width=125,height=30)
entry_number = Entry(window2)
entry_number.grid(row = 2 , column=2 ,  sticky='WEN' )
# END
mainloop()
