class Student:
     num_students = 0
     class_year = 2025
     def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print((f"{student1.name} graduating year: {Student.class_year}"))
