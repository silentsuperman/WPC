class good():
	def display(self,name=None,age=None):
		if(name == None and age ==None):
			print("No arguement is passed")
		elif(name!=None and age==None):
			print(name)
		elif(name!=None and age!=None):
			print(name,age)
		else:
			print("hehe")
g=good()
g.display()
g.display("shashank")
g.display("shash",20)


#using variable length argument

def area(*v):
	if(len(v)==0):
		print("No arguement is passed")
	elif(len(v)==1):
		print("Area of square is",v[0]*v[0])
	elif(len(v)==2):
		print("Area of rectangle is",v[0]*v[1])
	else:
		print("Invalid arguements")
		
area()
area(4)
area(4,5)
