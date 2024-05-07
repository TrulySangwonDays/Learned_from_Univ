### 20201929 이상원 ###

while True :
    start_num = input('프로그램 실행 번호 (1~3, end:종료) : ')

    if start_num == '1' :
        
        ## 1번 답안 20201929 이상원 ##
        number, hour, minute, second = 0, 0, 0, 0

        number = int(input("초 입력: "))                    # 초 입력
        hour = number // 3600                               # 입력받은 수(초)를 3600으로 나눈 몫 <- 시간 단위
        minute = (number % 3600) // 60                      # 3600으로 나눈 "나머지"를 60으로 나눈 몫 <- 분 단위
        second = (number % 3600) % 60                       # 3600으로 나눈 "나머지"를 60으로 나눈 "나머지" <- 초 단위
        if hour!=0 and minute!=0 and second!=0 :            # 시간, 분, 초 단위가 모두 0이 아니면 -> 00시간 00분 00초
            print(f'{hour}시간 {minute}분 {second}초')
        elif hour!=0 and minute!=0 and second==0 :          # 시간, 분 단위가 0 아니고, 초 단위가 0이면 -> 00시간 00분
            print(f'{hour}시간 {minute}분')
        elif hour!=0 and minute==0 and second==0 :          # 시간 단위가 0이 아니고, 분,초 단위가 0이면 -> 00시간
            print(f'{hour}시간')
        elif hour==0 and minute!=0 and second!=0 :          # 시간 단위가 0이고, 분,초 단위가 0이 아니면 -> 00분 00초
            print(f'{minute}분 {second}초')
        elif hour==0 and minute!=0 and second==0 :          # 시간,초 단위가 0이고 분 단위가 0이 아니면 -> 00분
            print(f'{minute}분')
        elif hour==0 and minute==0 and second!=0 :          # 시간,분 단위가 0이고 초 단위가 0이 아니면 -> 00초
            print(f'{second}초')
        
        
    elif start_num == '2' :
        
        ## 2번 답안 20201929 이상원 ##
        i = 1
        while i < 10 :
            j = 2
            while j < 10 :
                if (i == 3) or (j == 3) or ((i * j)%10 == 3) or ((i * j)//10 == 3):
                    print('', end='\t')
                else :
                    val = i * j
                    print(f'{j}X{i}={val}', end='\t')
                j += 1
            print('')
            i += 1
        
        
    elif start_num == '3' :

        ## 3번 답안 20201929 이상원 ##
        import random
        Num = int(input('2보다 큰 정수를 입력: '))

        if Num > 2 :
            List = []
            count = 0

            while True :
                count += 13
                ready_to_append = random.randint(1, Num)

                if ready_to_append in List :
                    List.append(ready_to_append)
                    break

                List.append(ready_to_append)

            print(f'{count}번 무작위 수를 만들었습니다.')
            print(f'숫자는 {List} 입니다.')

        else :
            print('2보다 큰 정수를 입력하세요.')        
        
        
    elif start_num == 'end' :
        print('=============== 프로그램 종료 ===============')
        break
    
    
    else :
        print('잘못된 입력입니다.')
        continue

print()
exit()
