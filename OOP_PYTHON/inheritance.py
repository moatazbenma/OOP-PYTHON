class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        return f"my name is {self.name} and age is {self.age}"
    

class Women(Person):
    no_of_women = 0
    
    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Women.no_of_women += 1
        
    def display(self):
        string = super().display()
        return string + f" and my hair is {self.hair}"
        
      
  
women = Women("samira", 40, "curly")
print(women.display())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        