from tkinter import *

num = 0
def Write7():
    global num
    entry.insert(num, "7")
    num += 1
def Write8():
    global num
    entry.insert(num, "8")
    num += 1
def Write9():
    global num
    entry.insert(num, "9")
    num += 1
def Write4():
    global num
    entry.insert(num, "4")
    num += 1
def Write5():
    global num
    entry.insert(num, "5")
    num += 1
def Write6():
    global num
    entry.insert(num, "6")
    num += 1
def Write1():
    global num
    entry.insert(num, "1")
    num += 1
def Write2():
    global num
    entry.insert(num, "2")
    num += 1
def Write3():
    global num
    entry.insert(num, "3")
    num += 1
def Write0():
    global num
    entry.insert(num, "0")
    num += 1
def Write점():
    global num
    entry.insert(num, ".")
    num += 1
def Write나누기():
    global num
    entry.insert(num, "/")
    num += 1
def Write곱하기():
    global num
    entry.insert(num, "*")
    num += 1
def Write빼기():
    global num
    entry.insert(num, "-")
    num += 1
def Write더하기():
    global num
    entry.insert(num, "+")
    num += 1
    
def reset():
    global num
    entry.delete(0,END)
    num = 0

def Write등호():
    계산값 = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, 계산값)    

window=Tk()
window.title("계산기")

btn7 = Button(window, text="7", width="5", height="1", command=Write7)
btn8 = Button(window, text="8", width="5", height="1", command=Write8)
btn9 = Button(window, text="9", width="5", height="1", command=Write9)
btn4 = Button(window, text="4", width="5", height="1", command=Write4)
btn5 = Button(window, text="5", width="5", height="1", command=Write5)
btn6 = Button(window, text="6", width="5", height="1", command=Write6)
btn1 = Button(window, text="1", width="5", height="1", command=Write1)
btn2 = Button(window, text="2", width="5", height="1", command=Write2)
btn3 = Button(window, text="3", width="5", height="1", command=Write3)
btn0 = Button(window, text="0", width="5", height="1", command=Write0)
btn점 = Button(window, text=".", width="5", height="1", command=Write점)
btn등호 = Button(window, text="=", width="5", height="1", command=Write등호)
btn나누기 = Button(window, text="/", width="5", height="1", command=Write나누기)
btn리셋 = Button(window, text="C", width="5", height="1", command=reset)
btn곱하기 = Button(window, text="*", width="5", height="1", command=Write곱하기)
btn빼기 = Button(window, text="-", width="5", height="1", command=Write빼기)
btn더하기 = Button(window, text="+", width="5", height="1", command=Write더하기)
btn_empty1 = Button(window, width="5", height="1")
btn_empty2 = Button(window, width="5", height="1")
btn_empty3 = Button(window, width="5", height="1")
entry = Entry(window, width=31, bg="yellow")

entry.grid(row=0, column=0, columnspan=5)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn0.grid(row=4, column=0)
btn점.grid(row=4, column=1)
btn등호.grid(row=4, column=2)
btn나누기.grid(row=1, column=3)
btn리셋.grid(row=1, column=4)
btn곱하기.grid(row=2, column=3)
btn빼기.grid(row=3, column=3)
btn더하기.grid(row=4, column=3)
btn_empty1.grid(row=2, column=4)
btn_empty2.grid(row=3, column=4)
btn_empty3.grid(row=4, column=4)


window.mainloop()














