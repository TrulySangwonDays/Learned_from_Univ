# csv 파일 
import csv

with open("sample.csv", mode="r") as f :
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        age = 2021 - int(row[3]) + 1
        print('이름 : %s\t키 : %s\t몸무게 : %s\t나이 : %s\t혈액형 : %s\t' %(row[0], row[1], row[2], row[3], row[4]))


# 문제4) BMI 계산하기
import csv

with open("sample.csv", mode="r") as f :
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        height = int(row[1])/100
        weight = int(row[2])
        BMI = weight / (height*height)
        if BMI < 18.5 :
            state = "저체중"
        elif BMI < 25 :
            state = "정상체중"
        elif BMI < 30 :
            state = "과체중"
        elif BMI < 35 :
            state = "비만"
        elif BMI < 40 :
            state = "고도비만"
        else:
            state = "초고도비만"

        print("이름 : %s\tBMI : %.2f\t체중상태 : %s" %(row[0], BMI, state))

# csv 파일 쓰기
import csv
data = []
data.append(["Jin", 179, 64])
data.append(["Suga", 174, 59])

with open("test.csv", "w", newline="") as f:
    wr = csv.writer(f)
    for row in data:
        wr.writerow(row)

# 문제5) 문제4 BMI 계산 결과를 파일로 보내기
import csv

data = []
with open("sample.csv", mode="r") as f :
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        height = int(row[1])/100
        weight = int(row[2])
        BMI = weight / (height*height)
        if BMI < 18.5 :
            state = "저체중"
        elif BMI < 25 :
            state = "정상체중"
        elif BMI < 30 :
            state = "과체중"
        elif BMI < 35 :
            state = "비만"
        elif BMI < 40 :
            state = "고도비만"
        else:
            state = "초고도비만"

        print("이름 : %s\tBMI : %.2f\t체중상태 : %s" %(row[0], BMI, state))
        data.append([row[0], BMI, state])

with open("result.csv", "w", newline = "") as f:
    wr = csv.writer(f)
    wr.writerow(['이름', 'BMI', '체중상태'])
    for row in data:
        wr.writerow(row)

print()

# 정형데이터 & 비정형데이터
##import csv
##with open("NHIS_OPEN_T20_2016.csv", "r") as f:
##    csv_data = csv.reader(f)
##    next(csv_data)
##    for row in csv_data:
##        print(row)

#실습) 나이 조건으로 진료 인원수 파악하기
import csv
cnt = 0
with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        age_code = int(row[4])
        if age_code == 9:
            cnt =+ 1
print("40~44세 진료환자 수는 %d명입니다." %cnt)


#문제1) 서울에서 진료받은 외래환자 수 출력하기
import csv

cnt = 0
with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        sido = int(row[5])
        p_type = int(row[7])
        if sido == 11:
            if p_type == 3 or p_type == 8 or p_type == 11 :
                cnt += 1

print("서울에서 진료한 외래환자 수는 %d명입니다." %cnt)


#문제2) 인천에서 안과진료를 받은 50대여성 처방일수 출력하기
import csv

total = 0
data = []

with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        sex = int(row[3])
        sido = int(row[5])
        age_code = int(row[4])
        medical_tr = int(row[8])
        pres_days = int(row[17])
        if sex == 2 and sido == 28:
            if age_code == 11 or age_code == 12 :
                if medical_tr == 12 :
                    data.append(pres_days)
                    print("처방일 수 : %d" %pres_days)
for days in data:
    total += days
print("평균 처방일 수 : %.2f days" %(total/len(data)))


#문제3) 나이대 별 환자 수를 모두 집계해서 출력하기
import csv
ages = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        age_code = int(row[4])
        ages[age_code-1] = ages[age_code-1] + 1   # 아래 주석으로 한 것 한번에 표현
##        if age_code == 1:
##            ages[0] += 1
##        elif age_code == 2:
##            ages[1] += 1
##        elif age_code == 3:
##            ages[2] += 1
##        elif age_code == 4:
##            ages[3] += 1
##        elif age_code == 5:
##            ages[4] += 1
##        elif age_code == 6:
##            ages[5] += 1
##        elif age_code == 7:
##            ages[6] += 1
##        elif age_code == 8:
##            ages[7] += 1
##        elif age_code == 9:
##            ages[8] += 1
##        elif age_code == 10:
##            ages[9] += 1
##        elif age_code == 11:
##            ages[10] += 1
##        elif age_code == 12:
##            ages[11] += 1
##        elif age_code == 13:
##            ages[12] += 1
##        elif age_code == 14:
##            ages[13] += 1
##        elif age_code == 15:
##            ages[14] += 1
##        elif age_code == 16:
##            ages[15] += 1
##        elif age_code == 17:
##            ages[16] += 1
##        elif age_code == 18:
##            ages[17] += 1
##        else:
##            ages[1] += 1        
        
for i in range(len(ages)):
    print("Age %d ~ %d : %d" %(i*5, i*5+4, ages[i]))


# 문제4) 제주에서의 모든 진료 내역을 csv 파일로 저장하기
import csv

medical_history = []
with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    header = next(csv_data)
    for row in csv_data:
        sido = int(row[5])
        if sido == 49:
            medical_history.append(row)

with open("JEJU_HISTORY.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(header)
    for row in medical_history:
        wr.writerow(row)
























