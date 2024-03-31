from tkinter import *

window = Tk()


# 엔트리(Entry) 위젯
# 엔트리란, 텍스트를 한 줄 입력할 수 있는 상자 제공. Entry(부모, 속성..)
entry1 = Entry(window, width=30, bg="light green")
entry1.insert(0, "좋은 날씨네요.")
entry1.insert(0, "안녕하세요. ")
entry1.pack()

# 텍스트(text) 위젯
text1 = Text(window, width=20, height=10, bg="pink")
text1.insert(1.0, "AAAAAAAA\n") #1행 0인덱스
text1.insert(2.0, "BBBBBBBB\n") #2행 0인덱스
text1.insert(2.0, "CCCCCCCC\n") #3행 0인덱스
text1.insert(1.1, "D")          #1행 1인덱스
text1.pack()
print(text1.get(1.0,END))

window.mainloop()




#------------------------------------------

from tkinter import *

# 버튼(Button)
# 버튼이란, 클릭하면 눌리는 효과와 함께 지정한 작업 실행. Button(부모, 속성...)
def myFunc():
    value = entry1.get()
    print(value)
    return

window = Tk()
    
entry1 = Entry(window, width=30, bg="light blue")
entry1.pack()
button1 = Button(window, text="엔트리 읽기", command=myFunc)
button1.pack()

window.mainloop()



## 문제1) 섭씨 -> 화씨 변환 프로그램
from tkinter import *

def CtoF():
    celsius = float(entry1.get())
    fahrenheit = (celsius * 1.8) + 32
    entry2.delete(0,END)
    entry2.insert(0,fahrenheit)
    

window = Tk()

label1 = Label(window, text="섭씨")
label1.pack()

entry1 = Entry(window, width=20, bg="light green")
entry1.pack()

label2 = Label(window, text="화씨")
label2.pack()

entry2 = Entry(window, width=20, bg="pink")
entry2.pack()

button1 = Button(window, text="섭씨->화씨", command=CtoF)
button1.pack()


window.mainloop()


## 문제2) 좋아하는 동물 사진보기
from tkinter import *
def nextImage():
    global current_image
    current_image = current_image + 1
    if current_image>2:
        current_image=0
    label1["image"] = photo_list[current_image]
    
window = Tk()

photo_list=[]
photo_list.append( PhotoImage(file="아린.gif") )
photo_list.append( PhotoImage(file="fafa.gif") )
photo_list.append( PhotoImage(file="꽃.gif") )
current_image = 0

button1 = Button(window, text="다음 사진", command=nextImage)
label1 = Label(window, image=photo_list[current_image])

button1.pack()
label1.pack()

window.mainloop()


# 실습) (별로 안 중요한 내용) gif 이미지파일을 버튼에 표시하기
from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("아린 버튼", "아린 이쁘죠?")

window = Tk()
photo = PhotoImage(file="아린.gif")
button1 = Button(window, image=photo, command=myFunc)
button1.pack()

window.mainloop()
































