#***********************************************#

def note_count(abc):
    abc = abc[:-1]
    list1 = abc.split(":")
    StudentName = list1[0]
    StudentGrade= list1[1].split(",")

    note1 = int(StudentGrade[0])
    note2 = int(StudentGrade[1])
    note3 = int(StudentGrade[2])

    gpa = (note1 + note2 + note3)/3
    
    if gpa <= 100 and gpa >= 90:
        letter = "AA"
    elif gpa <=89 and gpa >=85:
        letter = "BA"
    elif gpa <=84 and gpa >=80:
        letter = "BB"
    elif gpa <=79 and gpa >=75:
        letter = "CB"
    elif gpa <=74 and gpa >70:
        letter = "CC"
    elif gpa <=69 and gpa >=65:
        letter = "DC"
    elif gpa <=64 and gpa >=60:
        letter = "DD"
    elif gpa <=59 and gpa >=50:
        letter = "FD"
    elif gpa <=49 and gpa >=0:
        letter = "FF"
    else:
        print("Incorrect average calculation, please enter a score between 0-100.")
    
    return StudentName + ": "+ letter + "\n"

 #***********************************************#
 #***********************************************#
 
def read_note():
    with open("StudentGrades.txt","r",encoding="utf-8") as file:
        for abc in file:
            print("********\n"+note_count(abc))

#***********************************************#

def enter_note():
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    grade1 = input("Note 1 : ")
    grade2 = input("Note 2 : ")
    grade3 = input("Note 3 : ")

    with open("StudentGrades.txt","a",encoding="utf-8") as file:
        file.write(name+" "+surname+":"+grade1+","+grade2+","+grade3+"\n")

    #***********************************************#

def save_note():
    with open("StudentGrades.txt","r",encoding="utf-8") as file:
        listresult = []

        for i in file:
            listresult.append(note_count(i))

        with open("ResultGradeS.txt","w",encoding="utf-8") as file2:
            for i in listresult:
                file2.write(i)

    #***********************************************#
        
while True:
    process = input("1- Read Note\n2- Enter Note\n3- Save Notes\n4- Exit\n:")
    
    if process == "1":
        read_note()

    if process == "2":
        enter_note()

    if process == "3":
        save_note()
        print("Notes Saved.")

    if process == "4":
        print("Bye")
        break

    #***********************************************#