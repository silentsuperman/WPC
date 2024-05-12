class student:
	def __init__(self):
		self.usn=input("Enter USN:")
		self.name=input("Enter Name:")
		self.age=int(input("Enter Age:"))
	def display(self):
		print("Name:",self.name)
		print("USN:",self.usn)
		print("Age:",self.age)
class ugstudent(student):
	def __init__(self):
		student.__init__(self)
		self.sem=input("Enter semster:")
		self.fees=int(input("Enter fee"))
		self.stipend=int(input("Enter stipend:"))
		ugstudent.display(self)
	def display(self):
		student.display(self)
		print("SEMESTER :",self.sem)
		print("FEE :",self.fees)
		print("STIPEND :",self.stipend)

class pgstudent(student):
	def __init__(self):
		student.__init__(self)
		self.sem=input("Enter semster:")
		self.fees=int(input("Enter fee:"))
		self.stipend=int(input("Enter stipend:"))
		pgstudent.display(self)
	def display(self):
		student.display(self)
		print("SEMESTER :",self.sem)
		print("FEE :",self.fees)
		print("STIPEND :",self.stipend)
while True:     
	print("1.ug\n2.pg\n0.exit ")
	ch=int(input("enter the choice:"))
	if ch==1:
		ug=ugstudent()
	elif ch==2:
		pg=pgstudent()
	elif ch==0:
		break
	else:
		print("wrong input")
	break