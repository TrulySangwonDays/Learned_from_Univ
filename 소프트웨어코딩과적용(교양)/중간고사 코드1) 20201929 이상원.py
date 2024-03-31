student_list = []
student_list.append({"학번":1000, "이름":"홍길동", "학과":"열공학과"})
student_list.append({"학번":1001, "이름":"강감찬", "학과":"체육학과"})
student_list.append({"학번":1002, "이름":"이순신", "학과":"물리학과"})
student_list.append({"학번":1003, "이름":"신사임당", "학과":"열공학과"})

while True:
    print("┌────────────────────────────────────────────────────┐")
    print("│ 학생관리 프로그램 V 1.0 created by 이상원            │")
    print("├────────────────────────────────────────────────────┤")
    print("│ 1. 전체출력  2. 검색  3. 신규 학생추가     0. 종료   │")
    print("└────────────────────────────────────────────────────┘")
    number = int(input("명령을 입력해주세요 : "))

    while 3 < number :
        number = int(input("잘못된 명령입니다. 명령을 입력해주세요 : "))
        
    if number == 1:
        print()
        print("┌──────────────────────────────────────────┐")
        print("│ 전체 학생 목록                            │")
        print("└──────────────────────────────────────────┘")
        for i in student_list :
            print("학번 : %d, 이름 : %s, 학과 : %s" %(i["학번"], i["이름"], i["학과"]))

    if number == 2:
        print()
        print("┌──────────────────────────────────────────┐")
        print("│ 검색 메뉴를 선택하세요.                    │")
        print("├──────────────────────────────────────────┤")
        print("│ 1. 이름 검색    2. 학과 검색              │")
        print("└──────────────────────────────────────────┘")
        number_search = int(input("검색 메뉴를 선택하세요 : "))

        while 2 < number_search :
            number_search = int(input("잘못된 명령입니다. 명령을 입력해주세요 : "))

        count_search = 0
        if number_search == 1:
            name_search = input("검색할 이름을 입력하세요 : ")
            for data in student_list:
                if data["이름"] == name_search:
                    print("학번 : %d, 이름 : %s, 학과 : %s" %(data["학번"], data["이름"], data["학과"]))
                    count_search += 1
            if count_search == 0 :
                print("검색 결과가 없습니다.")
        if number_search == 2:
            dep_search = input("검색할 학과를 입력하세요 : ")
            for data in student_list:
                if data["학과"] == dep_search:
                    print("학번 : %d, 이름 : %s, 학과 : %s" %(data["학번"], data["이름"], data["학과"]))
                    count_search += 1
            if count_search == 0 :
                print("검색 결과가 없습니다.")

    if number == 3:
        print("신규 학생 정보를 등록합니다.")
        print()
        id_new = int(input("학번을 입력하세요 : "))
        name_new = input("이름을 입력하세요 : ")
        dep_new = input("학과를 입력하세요 : ")
        
        student_list.append({"학번":id_new, "이름":name_new, "학과":dep_new})
        print("신규 학생이 추가되었습니다.")

    if number == 0:
        break

    print()
    print("=== 출력 종료 ===")
    input("계속하려면 Enter키를 누르세요...")
    print()
    print("-----------------------------------------------------------------------")

print()
print("┌──────────────────────────────────────────┐")
print("│ 프로그램을 종료합니다.                     │")
print("└──────────────────────────────────────────┘")
