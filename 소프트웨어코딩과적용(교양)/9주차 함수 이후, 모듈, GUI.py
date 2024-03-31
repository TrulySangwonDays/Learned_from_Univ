## 함수 이어서

# 문제4) 로또 복권 번호 추첨 프로그램
import random

def makeSixNumbers() :
    lotto = []
    print("당첨 번호 추첨 중...", end="")
    while len(lotto) != 6 :
        num = random.randint(1,45)
        if lotto.count(num) == 0 :
            lotto.append(num)
            print("%d " %num, end="")
    print("완료되었습니다.")
    return lotto

print(" ** 로또 추첨을 시작합니다. ** ")
numbers = makeSixNumbers()
numbers.sort()
print("축하합니다! 1등 번호 ==> ", end="")
for i in numbers:
    print("%d " %i, end="")


# 함수에 여러 개의 입력값 전달하기
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1, 1) :
        sum += i
    return sum
print(get_sum(1,10))



# 변수의 종류
#   지역변수(local variable) : 함수 내부에서만 사용 가능
#   전역변수(global variable) : 실행코드 전체에서 접근 가능


def calculate_area(radius) :
    result = 3.14 * radius**2
    return result
r = float(input("원의 반지름 : "))
area = calculate_area(r)
print(area) # result는 지역변수이므로 전역변수 자리(area)에 result 넣으면 오류.


def calculate_ara(radius) :
    global area
    area = 3.14 * radius**2
area = 0
r = float(input("원의 반지름 : "))
calculate_area(r)
print(area)


# 모듈(Module)의 이해
# - 자주 사용하는 함수를 만들어 놓고, 해당 함수를 사용하기 위해 import를 사용

# Func.py 에 함수 정의
# A.py 에서 import.Func 선언하고 func1()



# GUI (Graphical User Interface)
# 사용자가 그래픽을 통해 컴퓨터와 작업할 수 있는 환경
# 마우스, 키보드 등을 이용하여 화면상의 위젯이나 메뉴를 사용


# Tkinter
from tkinter import *

window = Tk()

window.title("Python window") #창 제목 설정
window.geometry("400x400") #창 크기 설정
window.resizable(0,0) #창 크기고정 설정, 1로 설정하면 테두리 변경가능

button1 = Button(window, text="클릭하세요!") # "클릭하세요!" 글자를 갖는 버튼을 window 내에 생성
button1.pack() # window에 button1을 부착시켜 화면에 보이도록 함 

label1 = Label(window, text="파이썬 윈도우", width=30, height=5, bg="yellow", anchor=NW)
label2 = Label(window, text="라벨입니다", font=("궁서체",30), fg="blue")
label1.pack()
label2.pack()

label2.configure(text="안녕하세요!") #기존 생성된 라벨의 속성을 변경할 수 있음
label2['text'] = "안녕" #딕셔너리 코드 형태로도 속성 변경 가능

photo = PhotoImage(file="fafa.gif")
label3 = Label(window, image=photo)
label3.pack()


window.mainloop() #사용자 이벤트를 기다리는 용도로 항상 사용

















