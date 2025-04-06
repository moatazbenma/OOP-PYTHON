class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def print_all(self): #Polymorphism 
        print(self.name)
        print(self.age)
        print(self.salary)
        
        
class Employee(Person):
    def __init__(self, name, age, salary, hair):
        Person.__init__(self, name, age, salary)
        self.hair = hair
        
    def print_all(self): #Polymorphism we used this function in another class multiple times
    
        print(self.name)
        print(self.hair)
        
employee1 = Employee("mohamed", 20, 1400, "black")
employee1.print_all()
        