# 파일 입출력

##f = open("새 파일.txt", "w")
##
##for i in range(1, 11, 1):
##    data = "%d번째 줄입니다. \n" %i
##    f.write(data)
##
##f.close()

with open("새 파일.txt", "w") as f:
    for i in range(1, 11, 1):
        data = "%d번째 줄입니다. \n" %i
        f.write(data)

with open("새 파일.txt", "r") as f:
    data = f.read()
    print(data)


from tkinter import *
from tkinter import messagebox

def readfile():
    with open("새 파일.txt", "r") as f:
        data = f.read()
    text1.delete(1.0, END)
    text1.insert(1.0, data)

def writefile():
    data = text1.get(1.0, END)
    with open("새 파일.txt", "w") as f:
        f.write(data)
    messagebox.showinfo("알림", "저장되었습니다.")
    
window = Tk()

text1 = Text(window, width=40, height=20, bg="white")
button1 = Button(window, text="파일 불러오기", command=readfile)
button2 = Button(window, text="파일 저장하기", command=writefile)

text1.pack()
button1.pack()
button2.pack()

window.mainloop()




# csv 파일 
import csv

with open("sample.csv", "r") as f :
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row)


















