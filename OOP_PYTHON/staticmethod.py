class Dates:

    @staticmethod
    def add(x, y):
        return x + y
      
    @staticmethod
    def add5(num):
        return num + 5
        
    @staticmethod
    def add10(num):
        return num + 10
    
num = Dates.add(5, 10)
x = Dates.add5(num)
y = Dates.add10(x)
print(num, x, y)

        
