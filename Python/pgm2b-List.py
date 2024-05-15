l1=[1,5,2,9,6,4]
l2=[8,10,12]
f=1
while(f):
    print("\nMenu \n1.Concatenation \n2.Length \n3.Append \n4.Sum \n5.Maximum \n6.Minimum \n7.Sort \n8.Reverse the list \n9.pop"
    "\n10.Clear \n11.Exit")
    try:
        ch=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    if(ch==1):
        print("Concatenation of ",l1,"and",l2,"is:",l1+l2)
    elif(ch==2):
        print("Length of list ",l1,"is:",len(l1))
    elif(ch==3):
        ele=int(input("Enter a element to append:"))
        print("Before appending:",l1)
        l1.append(ele)
        print("After appending:",l1)
    elif(ch==4):
        if l1:
            print("Sum of all digits of the list",l1,"is:",sum(l1))
        else:
            print("List is empty.")
    elif(ch==5):
        if l1:
            print("Maximum value of the list",l1,"is:",max(l1))
        else:
            print("List is empty.")
    elif(ch==6):
        if l1:
            print("Minimum value of the list",l1,"is:",min(l1))
        else:
            print("List is empty.")
    elif(ch==7):
        print("Before sorting list:",l1)
        l1.sort()
        print("After Sorting list:",l1)
    elif(ch==8):
        print("Before reversing the list:",l1)
        l1.reverse()
        print("After Reversing the list:",l1)
    elif(ch==9):
        if l1:
            print("Popped element: ",l1.pop())
        else:
            print("List is empty.")
    elif(ch==10):
        print("Before clearing the list:",l1)
        l1.clear()
        print("After clearing the list:",l1)
    elif(ch==11):
        f=0
    else:
        print("Invalid Choice")