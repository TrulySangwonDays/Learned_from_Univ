import random

w = "이겼습니다!"
l = "졌습니다!"
d = "비겼습니다."

win = 0
lose = 0

while (win!=3 and lose!=3) :
    user = int(input("가위바위보를 선택하세요. (1.가위, 2.바위, 3.보) : " ))
    com = random.randint(1,3)
    print("==========================================")

    #사용자 선택값 출력
    if user == 1 :
        real_u = "가위"
    elif user == 2 :
        real_u = "바위"
    elif user == 3 :
        real_u = "보"
    print("당신의 선택은 (%s)입니다." %real_u)

    #컴퓨터 선택값 출력
    if com == 1 :
        real_c = "가위"
    elif com == 2 :
        real_c = "바위"
    elif com == 3 :
        real_c = "보"
    print("컴퓨터의 선택은 (%s)입니다." %real_c)

    #승자 계산 및 결과 출력
    if user == 1 :
        if com == 1 :
            결과 = d
        elif com == 2 :
            결과 = l
            lose = lose + 1
        elif com == 3 :
            결과 = w
            win = win + 1
    elif user == 2 :
        if com == 1 :
            결과 = w
            win = win + 1
        elif com == 2 :
            결과 = d
        elif com == 3 :
            결과 = l
            lose = lose + 1
    elif user == 3 :
        if com == 1 :
            결과 = l
            lose = lose + 1
        elif com == 2 :
            결과 = w
            win = win + 1
        elif com == 3 :
            결과 = d
    print("%s 현재 스코어 %d승 %d패" %(결과, win, lose))
    print("==========================================")
    print()


if win == 3 :
    print("먼저 3승을 했네요. 최종 승리!")
else :
    print("먼저 3패를 했네요.. 최종 패배!")


print()
print()
print()
input("종료")







