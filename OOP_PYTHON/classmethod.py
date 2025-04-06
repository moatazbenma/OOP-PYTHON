from datetime import date
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def initbirth(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

        
    def describe(self):
        print(f"hello my name is {self.name} i have {self.age}")
        

student_1 = student("mohamed", 40)
student_2 = student_1.initbirth("khaled", 1994)
student_2.describe()
student_1.describe()













