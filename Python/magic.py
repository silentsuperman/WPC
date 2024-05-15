from magic1 import ope

ob1 = ope()
ob2 = ope()

ob1.getElement()
ob2.getElement()

while True:
    print("\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.FloorDivision\n 0.Exit")
    ch = int(input("enter your choice: "))
    if ch == 1:
        result = ob1 + ob2
        print("After Addition : ", result)

    elif ch == 2:
        result = ob1 - ob2
        print("After Subtraction: ", result)

    elif ch == 3:
        result = ob1 * ob2
        print("After Multiplication: ", result)
    
    elif ch == 4:
        result = ob1 // ob2
        print("After Floor Division: ", result)
    
    else:
        break
