def check_security(password):
    password = str(password)

    number = "0123456789" ;     special_text = "!@#$%^&*()"
    result = ""
    length = "" ;     num_con = "" ;      spt_con = ""

    if len(password) > 7:
        length = ">7"
        for i in password:
            if i in number:
                num_con = "num_yes"
        for k in password:
            if k in special_text:
                spt_con = "spt_yes"

    if length == ">7" :
        if (num_con == "num_yes") and (spt_con == "spt_yes"):
            result = "안전"
        elif (num_con == "num_yes") and (spt_con == ""):
            result = "보통"
        elif (num_con == "") and (spt_con == "spt_yes"):
            result = "보통"
        else:
            result = "취약"
    else:
        result = "사용불가"

    return result

pwd = input("비밀번호를 입력하세요 : ")
print("보안상태는 [%s]입니다." %check_security(pwd))
