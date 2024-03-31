# 여러 데이터 관리하기

# - 리스트는 여러 데이터를 순차적으로 저장해 놓은 데이터들의 집합
# 리스트 = 대괄호 [  ]  로 묶어놓은 컨테이너 객체.

# 리스트이름 = [값1, 값2, 값3, ... ]     0부터 시작하는 번호를 사용
# 이 숫자를 '인덱스'라고 부른다.  표기방법 = 리스트이름[인덱스 번호]

aa = [10, 20, 30, 40]
print(aa)
print(aa[0])
print(aa[2])

# 데이터타입 출력
print(type(aa))
print(type(aa[0]))
print(type(aa[2]))


# 리스트 데이터 사용하기 (문자열)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
print(letters[0])
print()
print(type(letters))
print(type(letters[0]))

# 실습) 리스트에서 임의의 값 선택하기
import random
한식 = ['불고기', '제육볶음', '닭볶음탕', '김치찌개', '해물탕']
print("오늘의 추천 음식 : %s" %한식[random.randint(0, 4)])


# 문제1) 음식 추천 프로그램을 만들어보자
import random

한식  = ['된장찌개', '김치찌개', '미역국', '비빔밥']
중식 = ['짜장면', '짬뽕', '마라탕', '훠궈']
일식 = ['돈까스', '우동', '초밥', '가츠동']
양식 = ['스테이크', '파스타', '피자', '치킨']

print("어떤 음식 종류를 추천할까요?")
print("한식(1)  중식(2)  일식(3)  양식(4)  아무거나(5)")
answer = int(input("입력 : "))

if answer == 5: #아무거나
    answer = random.randint(1,4)

if answer == 1:
    print("오늘의 추천 음식 : %s" %한식[random.randint(0,4)])
elif answer == 2:
    print("오늘의 추천 음식 : %s" %중식[random.randint(0,4)])
elif answer == 3:
    print("오늘의 추천 음식 : %s" %일식[random.randint(0,4)])
elif answer == 4:
    print("오늘의 추천 음식 : %s" %양식[random.randint(0,4)])



# 실습
heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']
print("이름 : %s" %heroes[0])
print("이름 : %s" %heroes[1])
print("이름 : %s" %heroes[2])
print("이름 : %s" %heroes[3])

print()
# 인덱스 데이터가 많을 때.
for i in range(0, 4, 1):
    print("이름 : %s" %heroes[i])


# 문제2) 학생 점수의 평균값을 출력하시오.
scores = [ 85, 70, 90, 98, 87, 68, 77, 100, 75, 80]
total = 0
for i in range(0, 10, 1):
    total = total + scores[i]
print("학생 10명의 평균 점수는 %.2f 입니다." %(total/10))


# 리스트 사용시 주의할 점 - 인덱스는 정확히!
#    인덱스는 리스트 내의 데이터에 접근하기 위한 키(key)가 되므로 정확한 인덱스 번호 사용!
# range가 없는 for 루프를 이용하여 리스트 탐색하기
for i in [2, 30, 1, 100]:
    print(i)


# 실습) 앞의 문제2에서 작성한 학생 평균 점수 수정
scores = [ 85, 70, 90, 98, 87, 68, 77, 100, 75, 80]
total = 0
for data in scores:
    total = total + data
print("학생 10명의 평균 점수는 %.2f 입니다." %(total/10))


# 리스트의 데이터 값 변경하기
heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']
print(heroes)
heroes[1] = '닥터 스트레인지'
print(heroes)


# 리스트의 데이터 추가하기 ---- 리스트이름.append(값) -- 리스트의 맨뒤에 추가
aa = []
aa.append(10)
aa.append(20)
aa.append(30)
aa.append(40)
print(aa)
print(type(aa))


# 문제3) 369게임 결과를 리스트로 만들기(1~100까지)
                           #방법1
numbers = []
for i in range(1, 101, 1):
    if "3" in str(i):
        numbers.append("*")
    elif "6" in str(i):
        numbers.append("*")
    elif "9" in str(i):
        numbers.append("*")
    else:
        numbers.append(i)
print(numbers)

                           #방법2
numbers = []
for i in range(1, 101, 1):
    if ("3" in str(i)) or ("6" in str(i)) or ("9" in str(i)):
        numbers.append("*")
    else:
        numbers.append(i)
print(numbers)


############################ 리스트 객체의 다양한 함수들
#     리스트 ppt 표 참고
#     del(리스트이름[위치]) = 삭제
#     len(리스트이름) = 리스트 포함 항목 개수

# 데이터 추가하기(append, insert)
#    데이터 추가 : 리스트.append(값)
#    특정 위치에 끼워넣기 : 리스트.insert(위치, 값)

# 항목 삭제하기(remove, del)
#    항목 찾아서 삭제하기 : 리스트.remove(값)
#    인덱스로 삭제하기 : del(리스트[위치])

# pop
#    pop()은 리스트에서 마지막 항목을 꺼내옴과 동시에 삭제

# 리스트 탐색하기(index)
#    데이터를 이용하여 인덱스 위치 얻어내기 : 리스트.index(값)

# 리스트 내의 데이터 개수 세기(len)
#    print(len(리스트이름))

# 리스트 정렬하기(sort)
#    리스트이름.sort()

# 리스트 순서를 반대로 바꾸기(reverse)
#    리스트이름.reverse()

# 리스트에서 여러 항목 한번에 가져오기
#    슬라이싱(slicing)은 리스트에서 한번에 여러 개의 항목을 추출하는 기법
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0:3])
print(letters[:3]) #처음부터 3전까지
print(letters[3:]) #3부터 끝까지


###################### 튜플, 딕셔너리 ########################

# 튜플(Tuple)
#   튜플은 ( )로 생성. 항목을 "추가/변경/삭제" 할 수 없음(읽기전용)

tt1 = (10, 20, 30)
print(tt1)

tt2 = 10, 20, 30  #괄호 없어도 튜플로 인식
print(tt2)

# 튜플의 사용 - 사용할 때는 리스트와 마찬가지로 []로 이용함
tt1 = (10, 20, 30)
print(tt1[0] + tt1[1] + tt1[2])

# 다만, del(tt3) 이런 식으로 하면 튜플 자체는 삭제 가능



# 딕셔너리(Dictionary)
# 키(key)와 값(value)을 쌍으로 묶어서 데이터를 저장함
#      딕셔너리는 {}로 생성.
#      접근 방법 : 딕셔너리명[키] 하면 해당 원소에 접근

phone_book = {"홍":"1234", "강":"3333", "이":"2222"}
print(phone_book)

phone_book = {}
phone_book["홍"] = "1234"
phone_book["강"] = "3333"
phone_book["이"] = "2222"
print(phone_book)

print(phone_book["홍"])


# 딕셔너리의 활용
#    고유의 키와 내용을 갖는 데이터에 대한 관리  ex) 연락처, 어휘사전, 일기장




