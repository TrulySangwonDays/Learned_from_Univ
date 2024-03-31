# 형식 = for 변수 in range(반복수) :
#        반복실행할 코드

for i in range(5):
    print("환영합니다.")
    print("반갑습니다.")

print()

repeat = 5
for i in range(repeat):
    print("환영합니다.")


print()

# 문제1) n각형 그리기
import turtle
t= turtle.Pen()

n = int(input("몇각형을 그릴까요? : "))
angle = 360/n

for i in range(n):
    t.forward(100)
    t.right(angle)

## for 변수의 사용 예
for i in range(10) :
    print(i)


for i in range(0, 10, 1):
    print("i값 = %d" %i)


for i in range(1, 11, 1):
    print("i값 = %d" %i)


for i in range(1, 11, 2):
    print("i값 = %d" %i)


## 문제2) for문을 이용한 1~100까지 숫자 합 구하기
total = 0

for i in range(1, 101, 1):
    total = total + i   # totla += i 로 쓸 수도 있음
print(total)


# 짝수의 합
total = 0

for i in range(2, 101, 2):
    total = total + i   # totla += i 로 쓸 수도 있음
print(total)


# 홀수의 합
total = 0

for i in range(1, 101, 2):
    total = total + i   # totla += i 로 쓸 수도 있음
print(total)


# 입력값까지의 합
n = int(input("값을 입력하세요. : "))

total = 0

for i in range(1, n+1, 1):
    total = total + i   # totla += i 로 쓸 수도 있음
print(total)




#-----------------
# for문 과 while 반복문 비교

##변수 = 시작값
##while 변수값<끝값:
##    이 부분을 반복
##    변수=변수+증가


# 문제3) while로 작성했던 구구단을 for로 변경하기
dan = int(input("몇 단을 출력할까요? : "))

for i in range(1, 10, 1):
    print("%d X %d = %d" %(dan, i, dan*i))

# for문 안에 for문 중첩하여 사용하기
for i in range (0, 3, 1):
    for k in range (0, 2, 1):
        print("파이썬은 꿀잼 (i값: %d, k값: %d)" %(i, k))
# -> 바깥 3번 * 안쪽 3번 총 6번 실행



# 문제4) 구구단 2단부터 9단까지 전체 출력하기
for dan in range(2, 10, 1):
    for num in range(1, 10, 1):
        print("%d X %d = %d" %(dan, num, dan*num))
    print("==============")


# 문제5) 구구단 전체를 한 화면에 출력하기
for num in range(1, 10, 1):
    sentence = ""
    for dan in range(2, 10, 1) :
        sentence = sentence + "%d X %d = %d \t" %(dan, num, dan*num)
    print(sentence)

#또는
sentence = ""
for num in range(1, 10, 1):
    for dan in range(2, 10, 1) :
        sentence = sentence + "%d X %d = %d \t" %(dan, num, dan*num)
    sentence = sentence + "\n"
print(sentence)




## for 반복문의 다른 표기법 (range 함수 사용하지 않음)
    # range(1, 5, 1)은 리스트[1,2,3,4]와 같은 동작을 함
for i in [1,2,3,4]:
    print(i)

for i in [2, 30, 1, 100]:
    print(i)

for i in ["a","b","c","d"]:
    print(i)

a = "hello"
for i in a:
    print(i)


# 문제6) 입력 문장에서 글자 수 세기
sentence = input("영어 문장을 입력해보세요. : ")
find = input("어떤 글자를 찾을까요? : ")

count = 0
for i in sentence :    # sentence에서 문자열 하나씩 꺼내서 i에 대입
    if i == find :
        count += 1     # count = count + 1
    
print("입력한 문장에서 '%s'의 개수는 %d개입니다." %(find, count))



## 반복문을 탈출하는 break문
for i in range(1, 100):
    print("for문을 %d번 실행했습니다." %i)
    break

## 반복문 시작지점으로 다시 돌아가는 continue문
    # <1부터 100까지 출력하되 3의 배수는 지나치기>
for i in range(1, 101, 1):
    if i%3 == 0:
        continue
    print(i)


## 무한루프를 위한 while "True"
while True:
    print("ㅋ", end="")






