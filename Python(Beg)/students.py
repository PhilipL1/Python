#input_mark = int(input("Enter mark: "))  
#input_homework = int(input(" Homework: "))
#input_assessment= int(input(" Assessment: "))
#input_exam = int(input(" Final Exam: "))
class Student: 
    def __init__(self, name, age, cl = "student"):
        self.name=name
        self.age=age
        self.cl=cl
        
    def mark(self,input):
        if input > 85:
            return 'distinction'
        elif 65 <= input <= 85:
            return 'pass'
        else:
            return 'Fail'

    def final_grade(self,homework, assessment, exam):
        a= (homework/25)*100
        b= (assessment/50)*100
        c= (exam/100)*100
        grade = ((a *0.25)+ (b*0.5) + c) /1.75
        return grade
    
    def average_score(self, test_score):
        return sum(test_score)/len(test_score)
    
jill= Student("Jill","25",42)
print(f"Jill average score: {jill.average_score([43,70,56,84])}")
   
john = Student("John", "25")
mike = Student("Mike", "23")
m_grade = mike.final_grade(15, 25, 60)
print( "John: mark- " + john.mark(john.final_grade(15, 25, 60)) + " || final grade: " + str(john.final_grade(15, 25, 60)))
print(f"Mike: mark- {mike.mark(m_grade)} || final grade: {mike.final_grade(15, 25, 60)}")






