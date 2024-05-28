n1=input("Enter a First String")
n2=input("Enter a Second String")
while True:
    print('1.length of the string')
    print('2.concatenation of the string')
    print('3.Reverse of the string')
    print('4.Slicing operation')
    print('5.Repeat factor')
    print('6.isUpper')
    print('7.isLower')
    print('8.Iteration')
    print('9.startswith')
    print('10.endswith')
    print('11.count')
    print('12.Exit')

    ch=int(input('Enter the choice:'))
    if ch==1:
        print(len(n1))
    elif ch==2:
        print(n1+n2)
    elif ch==3:
        print(n1[::-1])
    elif ch==4:
        print(n1[1:4])
    elif ch==5:
        print(n1*2)
    elif ch==6:
        print(n1.isupper())
    elif ch==7:
        print(n1.islower())
    elif ch==8:
        for i in n1:
            print(i)
    elif ch==9:
        print(n1.startswith('H'))
    elif ch==10:
        print(n1.endswith('d'))
    elif ch==11:
        print(n1.count('H'))
    elif ch==12:
        break
    else:
        print('Invalid choice')