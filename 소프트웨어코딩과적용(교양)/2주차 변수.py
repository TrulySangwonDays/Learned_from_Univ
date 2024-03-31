x = 100
y = 200
print(x)
print(y)
print("안녕")
print(2345)
print("x")

a = 100
b = 50
result = a + b

print(result)
print(a,"+",b,"=", result)

name = "이상원"
address = "서울시 동작구 상도동"

print(name)
print(address)

#문자열 변수 더하기
x = "블랙"
y = "핑크"
z = x+y
print(z)
print()
print()

#파이썬 예약어는 변수 이름으로 사용할 수 없음
## print, import, 등등
### 기호, 특수 문자, 빈칸 사용 불가능
# 숫자로 시작할 수 없다. ex) 2nd_base (x)

#표기법
## 1. 밑줄 표기법 : my_new_car
## 2. 낙타 표기법 : myNewCar


#input() 명령어 - 키보드 입력을 받아 변수에 저장하기
##name = input("당신의 이름은 무엇입니까? :")
##print(name, "씨 반가워요.")
##print(name + "씨 반가워요.")
##print()



#문제1 - 로봇 기자 만들기
경기장 = input("경기장은 어디입니까? :")
이긴팀 = input("이긴 팀은 어디입니까? :")
loser = input("진 팀은 어디입니까? :")
스코어 = input("스코어는 몇대몇 입니까?:")
우수선수 = input("우수선수는 누구입니까?:")
print()
print("==============================")
print("오늘 "+경기장+"에서 축구 경기가 열렸습니다.")
print(이긴팀+ "와(과) "+loser+ "이(가) 치열한 공방전을 펼쳤습니다.")
print("결국 "+이긴팀+"이(가) "+loser+"을(를) "+스코어+" 로 이겼습니다.")
print(우수선수+"이(가) 맹활약하여 MVP로 선정되었습니다.")
print("==============================")
print()
print()

##문자열 내에 데이터 넣기 - 문자열 서식(format)
경기장 = input("경기장은? :")
print("오늘 %s에서 야구 경기가 열렸습니다." % 경기장)

name = "이상원"
address = "서울 동작구"
print("제 이름은 %s이고, %s에 살고 있습니다." %(name, address))
print()
print()

경기장 = input("경기장은 어디입니까? :")
이긴팀 = input("이긴 팀은 어디입니까? :")
loser = input("진 팀은 어디입니까? :")
스코어 = input("스코어는 몇대몇 입니까?:")
우수선수 = input("우수선수는 누구입니까?:")
print()
print("==============================")
print("오늘 %s에서 축구 경기가 열렸습니다." % 경기장)
print("%s와(과) %s이(가) 치열한 공방전을 펼쳤습니다." %(이긴팀, loser))
print("결국 %s이(가) %s을(를) %s로 이겼습니다." %(이긴팀, loser, 스코어))
print("%s이(가) 맹활약하여 MVP로 선정되었습니다." %우수선수)
print("==============================")
print()
print()



#정수 데이터 : %d d = 10진수 정수(Decimal) ============== cf. %s:문자열!!
name = "Sang_won"
age = 20
print("My name is %s, and I am %d." %(name, age))
print()

# %d 개수 꼭 맞추기 ex) print("%d" %(100,200)) (x) , print("%d %d" %100) (x)

#서식 실습
a = 100
b = 200
print(a, "+", b, "=", a+b)
print("%d + %d = %d" %(a, b, a+b))
print("%d+%d=%d" %(a, b, a+b))
print()
print()

#실수 데이터 : %f - 소수점 6자리까지 표현
print("%d / %d = %f" %(100, 200, 100/200))

# %.1f - 소수점 1자리까지 표현 ======== %.2f - 소수점 2자리까지 표현
# 나머지는 "반올림"함!!!
print("%d / %d = %.1f" %(100, 200, 100/200))

print()
# %s - 한 글자 이상의 문자열
# %d - 정수
# %f - 실수

#실습
a = 123
print("%d" %a)
print("%5d" %a) #5자리 공간에 쓰고, 빈자리는 띄어쓰기
print("%05d" %a) #5자리 공간에 쓰고, 빈자리에 0으로 채워라
print()

b = 123.45
print("%f" %b)
print("%.2f" %b)
print("%7.2f" %b) #7자리 공간에 쓰고, 빈자리는 띄어쓰기
print()

c = "Python"
print("%s" %c)
print("%10s" %c) #10자리 공간에 쓰고, 빈자리는 띄어쓰기
print()


# 이스케이프 문자를 이용한 서식 지정

#1 \n = 새로운 줄로 이동
#2 \t = tab키
#3 \\ = \를 출력
#4 \" = 따옴표(") 출력
print("어머니가 \"제발 잠 좀 자라\"라고 말씀하셨다.")
#4-1 따옴표 다른 방법
print('어머니가 "제발 잠 좀 자라"라고 말씀하셨다.')

## 문자열 앞에 r을 붙이면 이스케이프 문자를 처리하지 않음
print(r"\n \t \" \\를 그대로 출력")
print("\n \t \" \\를 그대로 출력")

print()

var2 = 200
var1 = var2 # var1 과 var2가 같다는 것이 아니라 var2의 내용물(값)만 var1으로 이동

# 자기 자신 값에 대한 계산 결과를 대입하는 방식
var1 = 100
var1 = var1 + 200 # 이렇게 하면 var1의 값이 300이 됨




