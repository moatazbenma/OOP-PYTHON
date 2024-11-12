class student:
    def __init__(self, name, age, courses):
        self.__name = name
        self.__age = age
        self.__courses = courses
        
    def get_name(self):
        return self.__name
        
    def set_name(self, new_name):
        self.__name = new_name
        
    def describe(self):
        print(f"hello my name is {self.__name} i have {self.__age}")
        
    def is_age(self, num):
        if self.__age >= num:
            print("you're old")
        else: 
            print("you're young")

student_1 = student("mohamed", 40, "math")
student_1.set_name("ahmed")
print(student_1.get_name())



