# 문제3) 좋아하는 동물 사진보기
from tkinter import *
def myFunc():
    if var.get()==1:
        label1.configure(image=photos[0])
    elif var.get()==2:
        label1.configure(image=photos[1])
    else:
        label1.configure(image=photos[2])

window=Tk()
photos = []
photos.append(PhotoImage(file="아린.gif"))
photos.append(PhotoImage(file="꽃.gif"))
photos.append(PhotoImage(file="fafa.gif"))

var = IntVar()
rb1 = Radiobutton(window, text="아린", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="꽃", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="fafa", variable=var, value=3, command=myFunc)
label1 = Label(window, image=photos[0])

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()



# 위젯 배치하기 방법1 (pack 배치)
from tkinter import *

window=Tk()

btnList=[]
for i in range(0,3,1):
    btnList.append( Button(window, text="버튼"+str(i+1)) )

for i in btnList:
    i.pack()

window.mainloop()



# 위젯 배치하기 방법2 (place 배치) - x,y좌표
from tkinter import *

window=Tk()
window.title("고정위치 배치하기")
window.geometry("210x210")

btnList=[]
for i in range(0,3,1):
    btnList.append(Button(window, text="버튼"+str(i+1)))

btnList[0].place(x=0, y=0)
btnList[1].place(x=80, y=80)
btnList[2].place(x=160, y=100)
window.mainloop()



# 위젯 배치하기 방법3 (grid 배치)
from tkinter import *

window=Tk()

btnList=[]
for i in range(0,3,1):
    btnList.append(Button(window, text="버튼"+str(i+1)))

btnList[0].grid(row=0, column=0)
btnList[1].grid(row=1, column=1)
btnList[2].grid(row=2, column=2)
window.mainloop()



# 문제4) 섭씨화씨 변환 프로그램 grid배치



































