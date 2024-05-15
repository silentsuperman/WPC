class ope:
    def __init__(self):
        self.l1=[]

    def getElement(self):
        n=int(input("Enter the number of elements: "))
        for i in range(0,n):
            element=int(input("Enter the element: "))
            self.l1.append(element)
        print("List is: ",self.l1)

    def __add__(self,other):
        l1=[]
        for i in range(0,len(self.l1)):
            l1.append(self.l1[i]+other.l1[i])   
        return l1

    def __sub__(self,other):
        l1=[]
        for i in range(0,len(self.l1)):
            l1.append(self.l1[i]-other.l1[i])   
        return l1

    def __mul__(self,other):
        l1=[]
        for i in range(0,len(self.l1)):
            l1.append(self.l1[i]*other.l1[i])   
        return l1
    
    def __floordiv__(self,other):
        l1=[]
        for i in range(0,len(self.l1)):
            l1.append(self.l1[i]//other.l1[i])   
        return l1
    

