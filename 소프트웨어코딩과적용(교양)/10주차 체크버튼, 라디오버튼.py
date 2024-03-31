## 체크버튼(Checkbutton)
from tkinter import *
from tkinter import messagebox

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

window = Tk()
chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)
cb1.pack()

window.mainloop()



## 라디오버튼(Radiobutton)
from tkinter import *
def myFunc():
    if var.get() == 1:
        label1.configure(text="아린")
    elif var.get() == 2:
        label1.configure(text="fafa")
    else:
        label1.configure(text="꽃")

window = Tk()
var = IntVar()
rb1 = Radiobutton(window, text="아린", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="fafa", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="꽃", variable=var, value=3, command=myFunc)

label1 = Label(window, text="선택한 그룹", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()




## 문제3) 좋아하는 동물 사진보기


















