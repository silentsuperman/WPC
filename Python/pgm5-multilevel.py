class Student:
    def getdata(self):
        self.name = input("Enter name: ")
        self.rollno = int(input("Enter rollno: "))
        self.age = int(input("Enter age: "))

class Marks(Student):
    def getmarks(self):
        self.marks1 = int(input("Enter marks: "))
        self.marks2 = int(input("Enter marks1: "))
        self.marks3 = int(input("Enter marks2: "))

class Result(Marks):
    def calc(self):
        self.total = self.marks1 + self.marks2 + self.marks3
        self.per = self.total / 3
        

    def display(self):
        print("Name: ", self.name)
        print("Rollno: ", self.rollno)
        print("Age: ", self.age)
        print("Marks1: ", self.marks1)
        print("Marks2: ", self.marks2)
        print("Marks3: ", self.marks3)
        print("Total: ", self.total)
        print("Percentage: ", self.per)
        
        
        if self.per >= 60:
            print("First Class")
        elif self.per >= 50:
            print("Second Class")
        elif self.per >= 40:
            print("Third Class")    
        else:
            print("Fail")
        


std1 = Result()
std1.getdata()
std1.getmarks()
std1.calc()
std1.display()