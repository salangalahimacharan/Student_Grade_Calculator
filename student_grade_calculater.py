print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

English = int(input("Enter English marks: "))
Maths = int(input("Enter Maths marks: "))
Science = int(input("Enter Science marks: "))
Social = int(input("Enter Social marks: "))
Computer = int(input("Enter Computer marks: "))

if (English<0 or English>100 or 
    Maths<0 or Maths>100 or 
    Science<0 or Science>100 or 
    Social<0 or Social>100 or 
    Computer<0 or Computer>100):

    print("Please enter marks between 0 to 100")
    
else:
    total = English + Maths + Science + Social + Computer
    total_marks = 500
    percentage = (total/total_marks)*100

    print("\n===== STUDENT REPORT =====\n")
    print("Student Name:",name)
    print("English: ",English)
    print("Maths: ",Maths)
    print("Science: ",Science)
    print("Social: ",Social)
    print("Computer: ",Computer)
    print("Total Marks: ",total,"/",total_marks)
    print("Percentage:",percentage,"%")

    if (English<35 or 
        Maths<35 or 
        Science<35 or 
        Social<35 or 
        Computer<35):
        print("Result: FAIL")
        print("Grade: F")
        print("Remarks: Needs Improvement")
    else:
        print("Result: PASS")

        if percentage >=90 :
            grade = "A+"
            student_class = "Distinction"
            remarks = "Outstanding"
        elif percentage >=80 :
            grade = "A"
            student_class = "First class"
            remarks = "Excellent"
        elif percentage >=70 :
            grade = "B"
            student_class = "First class"
            remarks = "Very good"
        elif percentage >=60 :
            grade = "c"
            student_class = "second class"
            remarks = "Good"
        else:
            grade = "D"
            student_class = "Third class"
            remarks = "pass"
        print("Grade  :",grade)
        print("class  :",student_class)
        print("Remarks  :",remarks)
        print("\nThank you for using student grade calculator")