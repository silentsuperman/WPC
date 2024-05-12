l=[]
n=int(input("Enter range"))
print("Enter the elements\n")
for i in range(0,n):
    l.append(int(input()))
print("list is ",l)
while True:
    print("1.append 2.insert 3.pop 4.remove 5.length 6.count 7.min max 8.sort 9.reverse 10.clear")
    ch=int(input("Enter the choice"))
    if ch==1:
        e=int(input("Enter ele"))
        l.append(e)
        print("ele",e,"is appended successfully")
        print(l)
    elif ch==2:
        e=int(input("Enter ele"))
        p=int(input("Enter position"))
        if p <= len(l):
            l.insert(p,e)
            print(e,"is inserted at ",p)
            print(l)
        else:
            print("Position out of range")
    elif ch==3:
        if l:
            print("popped ele=",l.pop())
        else:
            print("List is empty")
    elif ch==4:
        v=int(input("Enter value to remove"))
        if v in l:
            l.remove(v)
            print(l)
        else:
            print("Value not found in list")
    elif ch==5:
        print(len(l))
    elif ch==6:
        e=int(input("Enter ele"))
        print(l.count(e))
    elif ch==7:
        if l:
            print(min(l),max(l))
        else:
            print("List is empty")
    elif ch==8:
        l.sort()
        print(l)
    elif ch==9:
        l.reverse()
        print(l)
    elif ch==10:
        l.clear()
    else:
        break
print()