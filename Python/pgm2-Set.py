s1={2,3,5,7,4}
s2={10,9,2,4}
while True:
	print("Menu \n1.Length \n2.Union \n3.Intersection \n4.Symmetric Difference \n5.Subset \n6.Superset \n7.Update \n8.Add Single "\
	"element \n9.Clear \n10.Delete \n11.Exit")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		print("Length of set ",s1,"is: ",len(s1))
	elif(ch==2):
		print("Union Operation of ",s1,"and",s2,"is:",s1.union(s2))
	elif(ch==3):
		print("Intersection operation of ",s1,"and",s2,"is:",s1.intersection(s2))
	elif(ch==4):
		print("Symmetric Difference of ",s1,"and",s2,"is:",s1.symmetric_difference(s2))
	elif(ch==5):
		print(s1,"is subset of",s2,":",s1.issubset(s2))
	elif(ch==6):
		print(s1,"is superset of",s2,":",s1.issuperset(s2))
	elif(ch==7):
		print("before Updating:",s1)
		s1.update(s2)
		print("After Updating:",s1)
	elif(ch==8):
		ele=int(input("Enter a element to add:"))
		print("Before Adding element",s1)
		s1.add(ele)
		print("After adding element:",s1)
	elif(ch==9):
		print("Before Clearing the set:",s1)
		s1.clear()
		print("After Clearing:",s1)
	elif(ch==10):
		print("Before deleting:",s1)
		ele=int(input("Enter a element to delete:"))
		s1.discard(ele)
		print("After Deleting:",s1)
	elif(ch==11):
		f=0
	else:
		print("Invalid Choice")