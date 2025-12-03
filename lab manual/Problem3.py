sub1 = int(input("Enter marks in English: "))
sub2 = int(input("Enter marks in Computer: "))
sub3 = int(input("Enter marks in Physics: "))
sub4 = int(input("Enter marks in Chemistry: "))
sub5 = int(input("Enter marks in Maths: "))

Total_marks = sub1 + sub2 + sub3 + sub4 + sub5 
print("Total marks: ",Total_marks)

percentage = (Total_marks*100)/500
print("Percentage :",percentage)

if(100>=percentage>=90):
    grade = "A"

elif(90>percentage>=80):
    grade = "B"

elif(80>percentage>=70):
    grade = "C"

elif(70>percentage>=60):
    grade = "D"

elif(60>percentage>=50):
    grade = "E"

else:
    grade = "Fail"

print("Grades: ",grade)