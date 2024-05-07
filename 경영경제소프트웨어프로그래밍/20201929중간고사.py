### 20201929 이상원 ###

while True :
    start_num = input('프로그램 실행 번호 (1~3, end:종료) : ')

    if start_num == '1' :
        ## 1번 답안 20201929 이상원 ##
        import turtle
        list_1 = []
#        while 'end' not in list_1 :
#            for i in range(1, 9999999) :
#                aa = input(f'색상#{i} 입력: ')
#                list_1.append(aa)
        
    elif start_num == '2' :
        ## 2번 답안 20201929 이상원 ##
        import random

        how = ['+', '-', '*']
        how_go = random.choice(how)

        while True :
            if how_go == '+' :
                # 덧셈
                a_1 = random.randint(1, 99)
                a_2 = random.randint(1, 99)
                a_3 = a_1 + a_2
                a_ans = None
                
                a_ans = int(input(f'{a_1} + {a_2} = '))
                if a_ans != a_3 :
                    print('틀렸습니다.')
                    continue
                elif a_ans == a_3 :
                    print('정답입니다.')
                    break
                    
            elif how_go == '-' :
                # 뺄셈
                b_1 = random.randint(1, 99)
                b_2 = random.randint(1, 99)
                b_3 = b_1 - b_2
                b_ans = None
                
                b_ans = int(input(f'{b_1} - {b_2} = '))
                if b_ans != b_3 :
                    print('틀렸습니다.')
                    continue
                elif b_ans == b_3 :
                    print('정답입니다.')
                    break

            elif how_go == '*' :
                # 곱셈
                c_1 = random.randint(1, 9)
                c_2 = random.randint(1, 9)
                c_3 = c_1 * c_2
                c_ans = None
                
                c_ans = int(input(f'{c_1} * {c_2} = '))
                if c_ans != c_3 :
                    print('틀렸습니다.')
                    continue
                elif c_ans == c_3 :
                    print('정답입니다.')
                    break

        
        
    elif start_num == '3' :
        ## 3번 답안 20201929 이상원 ##
        cho_gi = int(input('초기투자금액을 입력하세요 : '))

        rate = 0.12
        gigan = 0
        value_forecasted = cho_gi

        while value_forecasted < 4000 :
            gigan += 1
            value_forecasted = cho_gi * (1+rate)**gigan

        year = gigan // 2
        if gigan % 2 == 1 :
            month = "6"
        elif gigan % 2 == 0 :
            month = ""

        print(f'투자금 {cho_gi}만원이 4000만원 이상이 되기 위해서는 {year}년 {month}개월이 필요하고 투자금은 {value_forecasted:.0f}만원이 됩니다.')
        
        
    elif start_num == 'end' :
        print('=============== 프로그램 종료 ===============')
        break
    
    
    else :
        print('잘못된 입력입니다.')
        continue

print()
exit()






