# 6주차 복습 및 용 조금 이어서

lst = ['데이터1', '데이터2']
print(lst[0], lst[1])

dic = {'첫번째':'데이터1', '두번째':'데이터2'}
print(dic['첫번째'], dic['두번째'])

# 실습) 학생 정보를 담는 딕셔너리를 생성해보자.

student1 = {'학번':1000, '이름':'홍길동', '학과':'경영학과'}
print(student1)

print("┌───────────────────────┐")
print("│ 학과 : %s\t│" %student1["학과"])
print("│ 학번 : %d\t\t│" %student1["학번"])
print("│ 이름 : %s\t\t│" %student1["이름"])
print("└───────────────────────┘")


# 새로운 키이면 추가, 기존에 있는 키이면 변경
student1["연락처"] = "010-1111-2222"   #추가
student1["학과"] = "파이썬학과"   #변경

print(len(student1))   # len : 원소 개수 세기

print()
print()


# 문제4) 학생정보를 리스트로 관리하고 탐색하기
student_list = []
student_list.append({'학번':1000, '이름':'홍길동', '학과':'열공학과'})
student_list.append({'학번':1001, '이름':'강감찬', '학과':'체육학과'})
student_list.append({'학번':1002, '이름':'이순신', '학과':'물리학과'})
student_list.append({'학번':1003, '이름':'신사임당', '학과':'열공학과'})

print("==모든 학생의 정보 출력==")
for data in student_list:
    print("┌───────────────────────┐")
    print("│ 학과 : %s\t│" %data["학과"])
    print("│ 학번 : %d\t\t│" %data["학번"])
    print("│ 이름 : %s\t\t│" %data["이름"])
    print("└───────────────────────┘")

print()

print("==모든 학생의 정보 출력==")
for i in range(0, len(student_list), 1):
    print("┌───────────────────────┐")
    print("│ 학과 : %s\t│" %student_list[i]["학과"])
    print("│ 학번 : %d\t\t│" %student_list[i]["학번"])
    print("│ 이름 : %s\t\t│" %student_list[i]["이름"])
    print("└───────────────────────┘")    


print()
print()
print()


# 문제4) 학생정보를 리스트로 관리하고 탐색하기(계속)
학과 = input("무슨 학과의 학생을 탐색할까요? : ")

print("==%s 학생의 정보 출력==" %학과)
for i in range(0, len(student_list), 1):
    if student_list[i]["학과"] == 학과:
        print("┌───────────────────────┐")
        print("│ 학과 : %s\t│" %student_list[i]["학과"])
        print("│ 학번 : %d\t\t│" %student_list[i]["학번"])
        print("│ 이름 : %s\t\t│" %student_list[i]["이름"])
        print("└───────────────────────┘")    

for data in student_list:
    if data["학과"] == 학과:
        print("┌───────────────────────┐")
        print("│ 학과 : %s\t│" %data["학과"])
        print("│ 학번 : %d\t\t│" %data["학번"])
        print("│ 이름 : %s\t\t│" %data["이름"])
        print("└───────────────────────┘")



#############################################################
# 7주차 - 함수


# 사용자 정의 함수 작성하고 호출하기
def calculate_area(radius):
    area = 3.14*radius**2
    return area

c1_area = calculate_area(5.0)
print(c1_area)
c2_area = calculate_area(3.0)
print(c2_area)



# 문제1) 섭씨 -> 화씨 변환 함수 만들기
def CtoF(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

c = int(input("섭씨 온도를 입력하세요 : "))
f = CtoF(c)
print("섭씨 %d도는 화씨 %.1f도 입니다." %(c, f))



# 문제2) 대/소문자 변환 함수

def change_case(text):
    result = ""
    
    for c in text:
        if c.isupper() == True:   #대문자이면
            result = result + c.lower()
        elif c.islower() == True:   #소문자이면
            result = result + c.upper()
        else:
            result = result + c
            
    return result

user_text = input("문자열을 입력하세요. : ")
print("%s를 %s로 변환하였습니다." %(user_text, change_case(user_text)))



# 문제3) 소수(prime number) 판별 함수 만들기

def isPrimeNumber(n):
    if n < 2:
        return False

    for i in range(2, n, 1):  # 2부터 n보다 작은 수까지 순회
        if n%i == 0:  # 자기보다 작은 수로 나눠졌다.
            return False

    return True    


number = int(input("숫자를 입력하세요 : "))

if isPrimeNumber(number) == True:
    print("%d은(는) prime number입니다." %number)
else :
    print("%d은(는) prime number가 아닙니다." %number)






















