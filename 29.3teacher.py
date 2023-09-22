#class will be teacher in it add this things given below
# classroom, subject, school, standard
class teacher:
    def __init__(self, classroom, subject, school):
        self.classroom = classroom
        self.subject = subject
        self.school = school

    def teach(self):
        print("i am teaching in class ", self.classroom)

    def syllabus(self):
        print("i am teaching this subject ", self.subject)

Quality_teacher = teacher("8-A", "maths", "navkar")
Quality_teacher2 = teacher("9-a", "science", "stkabir")

print(Quality_teacher.classroom)
print(Quality_teacher.subject)
print(Quality_teacher.school)
Quality_teacher.syllabus()
Quality_teacher2.syllabus()


print(Quality_teacher2.classroom)
print(Quality_teacher2.subject)
print(Quality_teacher2.school)