input_name = input("name: ")
input_homework = int(input(" Homework: "))
input_assessment= int(input(" Assessment: "))
input_exam = int(input(" Final Exam: "))

def final_grade(homework, assessment, exam):
    a= (homework/25)*100
    b= (assessment/50)*100
    c= (exam/100)*100
    return((a *0.25)+ (b*0.5) + c) /1.75
   
print( input_name + "'s final grade is :  " + str(final_grade(input_homework, input_homework, input_examp)))