#간단한 덧셈 계산기
num1 = input("첫 번째 숫자를 입력하세요 : ")
num2 = input("두 번째 숫자를 입력하세요 : ")

num3 = num1 + num2
print(num3) #문자열로 인식됨
#print("%d + %d = %d" %(num1, num2, num3))

#input() 으로 입력받은 데이터는 항상 '문자열'로 인식됨
# 정수(integer)로 변환해야 계산 가능 -> int() 함수로 해결 [형변환]

a = int("300")
b = int("200")
print(a + b)


num1 = input("첫 번째 숫자를 입력하세요 : ")
num2 = input("두 번째 숫자를 입력하세요 : ")

num1 = int(num1)
num2 = int(num2)
num3 = num1 + num2

print(num3)
print("%d + %d = %d" %(num1, num2, num3))

#----------응용
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

print("%d + %d = %d" %(num1, num2, num1 + num2))



# 문제3 터틀 객체로 사각형 그리기
가로 = int(input("사각형의 가로 길이를 입력하세요. : "))
세로 = int(input("사각형의 세로 길이를 입력하세요. : "))

import turtle
t = turtle.Pen()

t.forward(가로)
t.right(90)
t.forward(세로)
t.right(90)
t.forward(가로)
t.right(90)
t.forward(세로)
t.right(90)

# while 명령어 [ ~까지 반복 구문] -> while length < 500
# (실습) 변수의 활용 : 소용돌이 그리기

import turtle
t = turtle.Pen()

t.shape("turtle")
t.speed(0)

length = 1
while length < 30 :
    t.forward(length)
    t.right(179)
    length = length + 1


# 2교시 [연산자와 수식]

#수식(expression) : 피연산자들과 연산자의 조합
#연산자(operator) : 연산을 나타내는 기호
#피연산자(operand) : 연산의 대상이 되는 값

# / : 나누기 a = 5/3
# // : 나누기(몫) a = 5/3 일 때 5를 3으로 나눈 뒤 소수점을 버리고 a에 대입
# % : 나머지값 a = 5%3 일 때 5를 3으로 나눈 나머지
# ** : 제곱 a = 5**3 이면 5의 세제곱

a = 5/3 #실수값
print(a)

a = 5//3 #정수값 [만약 5.0//3 이면 실수값]
print(a)

a = 5%3
print(a)

a = 5**3
print(a)


#문제1) 커피 가게 매출 계산하기

아메 = 2000
카페 = 3000
카푸 = 3500

아메_수량 = int(input("아메리카노 판매수 : "))
카페_수량 = int(input("카페라떼 판매수 : "))
카푸_수량 = int(input("카푸치노 판매수 : "))

sales = 아메 * 아메_수량
sales = sales + (카페 * 카페_수량)
sales = sales + (카푸 * 카푸_수량)

print("총 매출은 %d원 입니다." % sales)


#문제2) 화씨 온도를 섭씨로 변환하기
F = float(input("화씨 온도 : ")) #int는 정수값! 실수 쓰고 싶으면 float() 써야 함
C = (F-32)*5/9 #실수값 데이터임. 이유는 9로 나누어줬기 때문

print("섭씨 온도 : %.2f" % C) #소수점 개수 조절 -> %.2f



#문제3) 자동 판매기 프로그램

In = int(input("투입한 돈 : "))
Price = int(input("물건 값 : "))

change = In - Price
개수_500 = change//500
개수_100 = (change%500) // 100

print("거스름돈 : %d원" %change)
print("500원 동전의 개수 : %.0f" %개수_500)
print("100원 동전의 개수 : %.0f" %개수_100)



#문제4) 초를 입력받고 시간, 분, 초 로 환산하기

num = int(input("초 단위 시간을 입력하세요 : "))

seconds = num%60
minutes = (num//60)%60
hours = (num//60)//60

print("%d초는 환산하면 %d시간 %d분 %d초입니다." %(num, hours, minutes, seconds))


## += : a+=3 <=> a=a+3
## -=, *=, /=, //=, %=, **=


# ;는 한 문장이 끝났다는 의미
a = 10
a+=5 ; print(a)




# 관계 연산자 - bool타입 (boolean)
# == : 같다 - 두 값이 동일하면 참
# != : 같지 않다 - 두 값이 다르면 참
# > : 크다
# > : 작다
# >= : 크거나 작다

a = 100
b = 200
print( a==b, a!=b, a>b, a<b, a>=b, a<=b )
# warning a=b 연산자는 a가 b라는 것이 아니라 b를 a에 대입하라는 의미!

a = 99
if a<100 :
    print("100보다 작군요.")


# 문제5) 짝수/홀수 맞추기

num = int(input("숫자를 입력하세요 : "))
if num%2 == 0 :
    print("짝수입니다.")
if num%2 == 1 :
    print("홀수입니다.")










