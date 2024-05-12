import mysql.connector

class myDatabase:
        def __init__(self):
                self.db=mysql.connector.connect(host="172.16.34.114",user="1rv21mc056",password="1rv21mc056",auth_plugin="mysql_native_password",database="1rv21mc056")
                self.cur=self.db.cursor()
                self.createtable()

        def createtable(self):
                query=""" CREATE TABLE IF NOT EXISTS emp(slno INT PRIMARY KEY,name VARCHAR(20),address VARCHAR(30),empcode VARCHAR(10),dob DATE,age INT,
                mobile INT,status INt,des VARCHAR(10) )"""
                self.cur.execute(query)
                self.db.commit()
                print("Table added.")

        def insert(self,slno,name,address,empcode,dob,age,mobile,status,des):
                query=""" INSERT INTO emp(slno,name,address,empcode,dob,age,mobile,status,des) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
                values=(slno,name,address,empcode,dob,age,mobile,status,des)
                self.cur.execute(query,values)
                self.db.commit()
                print("record added")

        def show(self):
                self.cur.execute("SELECT * FROM emp")
                rows=self.cur.fetchall()
                for r in rows:
                        print(r)

        def modify(self,des,slno):
                query=""" UPDATE emp SET des=%s WHERE slno=%s """
                values=(des,slno)
                self.cur.execute(query,values)
                print("record modified")

        def delete(self,slno):
                query="""DELETE FROM emp WHERE slno=%s """
                values=(slno,)
                self.cur.execute(query,values)
                print("record deleted")


d=myDatabase()

while True:
        print("1.Create\n2.Retrieve\n3.Update\n4.Delte\n")
        c=int(input("Enter your choice:"))
        if(c==1):
                slno=int(input("Enter slno:"))
                name=input("Enter name:")
                address=input("Enter address:")
                empcode=int(input("Enter empcode:"))
                dob=input("Enter DOB:")
                age=int(input("Enter age:"))
                mobile=int(input("Enter mobile phone number:"))
                status=int(input("Enter status:"))
                des=input("Enter designation:")
                d.insert(slno,name,address,empcode,dob,age,mobile,status,des)
                print("Table added")

        elif(c==2):
                d.show()
        elif(c==3):
                slno=int(input("Enter slno:"))
                des=input("Enter new  designation:")
                d.modify(des,slno)
        elif(c==4):
                slno=int(input("Enter slno whose table will be deleted:"))
                d.delete(slno)
        else:
                break
