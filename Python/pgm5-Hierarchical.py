class Student:
    def getdata(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.usn = input("Enter USN: ")

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("USN: ", self.usn)


class UG(Student):
    def getdata(self):
        super().getdata()
        self.fees = int(input("Enter fees: "))
        self.course = input("Enter course: ")
        self.sem = int(input("Enter semester: "))

    def display(self):
        super().display()
        print("Fees: ", self.fees)
        print("Course: ", self.course)
        print("Semester: ", self.sem)


class PG(Student):
    def getdata(self):
        super().getdata()
        self.fees = int(input("Enter fees: "))
        self.course = input("Enter course: ")
        self.sem = int(input("Enter semester: "))

    def display(self):
        super().display()
        print("Fees: ", self.fees)
        print("Course: ", self.course)
        print("Semester: ", self.sem)


std1 = UG()
std2 = PG()

while True:
    print("1. UG")
    print("2. PG")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        std1.getdata()
        std1.display()
    elif ch == 2:
        std2.getdata()
        std2.display()
    else:
        break