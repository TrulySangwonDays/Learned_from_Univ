print()
print("4주차 : 3주차 내용 이어서, 조건문과 반복문")

# and : 둘 다 참이어야 참  ex) (a>100) and (a<200)
# or : 둘 중 하나만 참이어도 참 ex) (a==100) or (a==200)
# not

# 관계연산자, 논리연산자를 혼합한 if조건
print("나이가 10살 이상이고, 키가 135cm 이상이면 놀이기구를 탈 수 있다.")
age = int(input("나이가 10살 이상입니까? : "))
height = int(input("키가 135cm 이상입니까? :"))
if (age>=10) and (height>=135):
    print("놀이기구를 탈 수 있다.")

# 연산자 우선순위

# abs(-100)
# pow(a,b)
# max(1,2,3,4,5) min(1,2,3,4,5)
# round(2.555) -> 3
# round(2.555,2) -> 2.56


# 문제6) 두 점 사이의 거리 구하기
x1 = int(input("첫 번째 점의 x값을 입력하세요. : "))
y1 = int(input("첫 번째 점의 y값을 입력하세요. : "))
x2 = int(input("두 번째 점의 x값을 입력하세요. : "))
y2 = int(input("두 번째 점의 y값을 입력하세요. : "))

import math
distance = math.sqrt( pow((x1-x2),2) + pow((y1-y2),2) )

print("두 점 (%d, %d)와 (%d, %d) 사이의 거리는 %f 입니다." %(x1, y1, x2, y2, distance))


## 조건문과 반복문

# 코드 실행의 기본 구조
#1. 순차구조
#2. 선택구조
#3. 반복구조

# if
a = 10
if a < 20:
    print("a는 20보다 작습니다.")
print("종료")


# if-else 양자택일

# if-else 중첩하여 사용하기


# 문제1) 시험점수에 대한 학점 출력하기
score = int(input("성적을 입력하시오. : "))

if score >= 90 :
    grade = "A"
else :
    if score >= 80 :
        grade = "B"
    else :
        if score >= 70 :
            grade = "C"
        else :
            if score >= 60 :
                grade = "D"
            else :
                grade = "F"
print("%s학점 입니다." % grade)


# 다중 if를 위한 [if - elif - else] 구문 --> 챗봇 실습


#문제2) 사칙연산 계산기 만들기
첫 = int(input("첫 번째 값을 입력하세요. : "))
연산기호 = input("연산 기호를 입력하세요(+,-,*,/). : ")
두 = int(input("두 번째 값을 입력하세요. : " ))
print("=================================")

if 연산기호 == "+" :
    값 = 첫+두
elif 연산기호 == "-" :
    값 = 첫-두
elif 연산기호 == "*" :
    값 = 첫*두
elif 연산기호 == "/" :
    값 = 첫/두
else :
    print("오류입니다.")

if 연산기호 == "/" :
    print("%d %s %d = %.3f" %(첫, 연산기호, 두, 값))
else :
    print("%d %s %d = %d" %(첫, 연산기호, 두, 값))



## 반복구조 : 반복문을 이용한 실행흐름 제어

# for 명령문 -> 데이터를 관리할 때 유용하게 쓰임
# while 명령문 true 일 때 실행, false이면 반복문 종료

# while 반복문


# 문제3) 구구단 출력하기
dan = int(input("몇 단을 출력할까요? : "))
num = 1

while num < 10 :
    print("%d * %d = %d" %(dan, num, dan*num))
    num = num + 1


# 문제4) 비밀번호를 입력받아서 로그인하기

pw = input("비밀번호를 입력하세요. : ")
password = "123"

while pw != password :
    print("비밀번호가 틀렸습니다.")
    print("=========================")
    pw = input("비밀번호를 입력하세요. : ")
print("로그인 성공!")


# 실습4) 챗봇.py 확장
# in 함수!!


# 문제5) 숫자 맞추기 up&down 게임

import random #랜덤 함수를 사용하기 위한 설정

com = random.randint(1,100)

num = int(input("제가 생각한 숫자를 맞춰보세요(1~100) : "))

횟수 = 1

while num != com :
    if num < com :
        print("%d보다 더 큰 수를 입력하세요. Up up ~ " %num)
    else :
        print("%d보다 더 작은 수를 입력하세요. Down down ~ " %num)
    횟수 = 횟수 + 1
    num = int(input("숫자를 다시 입력하세요. : "))

print("%d! 정답입니다! %d회 시도하여 맞췄습니다." %(num, 횟수))


## 4주차 과제!! 컴퓨터와 가위바위보 게임하기





    














