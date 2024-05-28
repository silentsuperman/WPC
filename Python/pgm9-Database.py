import mysql.connector
def getConn():
        return mysql.connector.connect(host="172.16.34.43",user="mca097",password="mca097",database="db_mca097")
def createTable(conn):
        conn.cursor().execute("""CREATE TABLE IF NOT EXISTS emp(empid INT primary key,name varchar(45),address varchar(45),age INT,sal FLOAT,status INT) """)
        print("Table created")
def addData(conn,empid,name,address,age,sal,status):
        conn.cursor().execute("INSERT INTO emp(empid,name,address,age,sal,status) VALUES(%s,%s,%s,%s,%s,%s)",(empid,name,address,age,sal,status))
        conn.commit()
        print("emp details added successfully")
def deletEmp(conn,empid):
        conn.cursor().execute("DELETE FROM emp where empid=%s",(empid,))
        conn.commit()
        print("record deleted")
def updateEmp(conn,sal,empid):
        conn.cursor().execute("UPDATE emp set sal=%s where empid=%s",(sal,empid))
        conn.commit()
def searchEmp(conn,empid):
        cur=conn.cursor()
        cur.execute("SELECT * FROM emp where empid = %s",(empid,))
        emp=cur.fetchone()
        print("EmpId: ",emp[0])
        print("Empname: ",emp[1])
        print("Emp adrress:  ",emp[2])
        print("Emp age:  ",emp[3])
        print("Emp sal:  ",emp[4])
        print("search successfull")
def main():
        conn=getConn()
        while True:
                print("1.Create table\n2.Add Employee\n3.Search Employee\n4.Update Employee\n5.Delete Employee")
                print("Enter your choice:")
                choice = input()
                if(choice == "1"):
                        createTable(conn)
                elif(choice == "2"):
                        print("enter emp data")
                        empid=input("Enter empid:  ")
                        name=input("Enter Name:  ")
                        address=input("Enter address:  ")
                        age=input("Enter age:  ")
                        sal=input("Enter sal:  ")
                        status=input("Enter status:  ")
                        addData(conn,empid,name,address,age,sal,status)
                elif(choice == "3"):
                        empid=input("Enter empid to be searched:  ")
                        searchEmp(conn,empid)
                elif(choice == "4"):
                        empid=input("Enter empid to be updated:  ")
                        sal=input("Enter sal for the above empid to be updated:  ")
                        updateEmp(conn,sal,empid)
                elif(choice == "5"):
                        empid=input("Enter the empid to record a record:  ")
                        deletEmp(conn,empid)
                elif(choice == "6"):
                        break
                else:
                        print("Invalid choice!!!")
main()