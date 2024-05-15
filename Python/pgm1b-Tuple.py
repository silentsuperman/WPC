t1=(1,2,3)
t2=()  # Initialize t2 as an empty tuple

while True:
    print("\nTuple Operation Menu: \n1.Concatenation \n2.Length of the tuple \n3.Reverse the tuple\n4.slicing\n5.Iteration on tuple\n6.in operator"
" \n7.count \n8.Check 2 tuples or equal or not\n9.Minimum \n10.Maximum\n11.Exit")
    choice=int(input("Enter a choice: "))
    if(choice==1):
        t2=(4,'a',6)
        print("Concatenated tuple is: ",t1+t2)
    elif(choice==2):
        print("Length of the tuple is",len(t1))
    elif(choice==3):
        print("Reverse of the tuple is",t1[::-1])
    elif(choice==4):
        print("Slicing on the tuple ",t1,"is",t1[0:2])
    elif(choice==5):
        print("Iteration on tuple",t1)
        for i in  t1:
            print(i)
    elif(choice==6):
        print("1 in tuple ",t1,"is:",1 in t1)
    elif(choice==7):
        print("Total occurance of element 1 in tuple ",t1,"is:",t1.count(1))
    elif(choice==8):
        print(t1,"is equal to ",t2,t1 is t2)
    elif(choice==9):
        print("Minimum of tuple",t1,"is",min(t1))
    elif(choice==10):
        print("Maximum of tuple",t1,"is",max(t1))
    elif(choice==11):
        f=0
    else:
        print("invalid choice")


        