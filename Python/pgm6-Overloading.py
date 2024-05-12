class Person:
        name=None
        age=None
        def Hello(self, name=None,age=None):
                self.name=name
                self.age=age
                print("Name:", self.name,"Age:",self.age)

p1=Person()
p1.Hello()
p1.Hello('Shrininivas')   
p1.Hello('Kulkarni',23)
