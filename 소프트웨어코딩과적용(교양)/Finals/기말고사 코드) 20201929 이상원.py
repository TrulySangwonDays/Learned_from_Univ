members = []
members.append( ["Jin", "M", 179, 64, 1992, "O"] )
members.append( ["Suga", "M", 174, 59, 1993, "O"] )
members.append( ["J-Hope", "M", 177, 65, 1994, "A"] )
members.append( ["RM", "M", 181, 67, 1994, "A"] )
members.append( ["Jimin", "M", 173, 60, 1995, "A"] )
members.append( ["V", "M", 178, 63, 1995, "AB"] )
members.append( ["Jungkook", "M", 178, 66, 1997, "A"] )

abo = input("Input bloodtype:")
abo = abo.upper()


result = ""

for i in range(0, 7, 1):
    if members[i][5] == abo:
        result = result + members[i][0] + "\n"

print(result)


######################################

import csv
cnt = 0

with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        진료 = int(row[8])
        if 진료 == 1:
            cnt =+ 1
print("진료환자 수는 %d명" %cnt)


##################################



import csv

ages = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #연령대별 그룹 18종류
with open("NHIS_OPEN_T20_2016.csv", "r") as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        age_code = int(row[4])
        ages[age_code-1] = ages[age_code-1] + 1

for i in range(len(ages)):
    print("Age %d ~ %d : %d" %(i*10, i*10+9, ages[i]))



##################################



from tkinter import *

window = Tk()
entry1 = Entry(window, width=16)
btn1 = Button(window, width=4, height=5, text="BTN1")
btn2 = Button(window, width=10, height=1, text="BTN2")
btn3 = Button(window, width=4, height=1, text="BTN3")
btn4 = Button(window, width=4, height=1, text="BTN4")
btn5 = Button(window, width=4, height=3, text="BTN5")
label1 = Label(window, width=16, text="LABEL1", bg='white')
entry1.grid(row=0, column=0, columnspan=3 )
btn1.grid(row=1, column=0, rowspan=3)
btn2.grid(row=1, column=1, columnspan=2)
btn3.grid(row=2, column=1) 
btn4.grid(row=3, column=1)
btn5.grid(row=2, column=2, rowspan=2)
label1.grid(row=4, column=0, columnspan=3)

window.mainloop()

 
##########################################

with open("369.txt", "w") as f: 
    numbers = []
    for i in range(1, 10001, 1):
        if "3" in str(i):
            numbers.append("*")
        elif "6" in str(i):
            numbers.append("*")
        elif "9" in str(i):
            numbers.append("*")
            
        else:
            numbers.append(i)
    print(numbers)
##        data = numbers
##        f.write(data)


















