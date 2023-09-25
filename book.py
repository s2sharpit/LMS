
#Python Module: Book


from datetime import date,datetime,timedelta
import mysql.connector



def AddRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code: ")
        bname=input("Enter Book Name: ")
        bauthname=input("Enter Book Author's Name: ")
        bprice=int(input("Enter Book Price: "))
        publ=input("Enter Publisher of Book: ")
        qty=int(input("Enter Quantity Purchased: "))
        print("Enter Date of Purchase (Date/Month and year separately:)")
        DD=int(input("Enter Date: "))
        MM=int(input("Enter Month: "))
        YY=int(input("Enter Year: "))
        sql="insert into bookrecords values (%s,%s,%s,%s,%s,%s,%s)"
        val=(bcode,bname,bauthname,bprice,publ,qty,date(YY,MM,DD))
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Inserted Successfully..........")

    except Exception as ex:
        print(ex)
        
    mydb.close()






def DeleteRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code of Book to be Deleted from the Library: ")
        sql="delete from bookrecords where bookcode=%s"
        val=(bcode,)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Deleted Successfully..........")

    except Exception as ex:
        print(ex)
        
    mydb.close()






def SearchRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code to be Searched from the Library: ")
        sql="select * from bookrecords where bookcode=%s"
        val=(bcode,)
        mycursor.execute(sql,val)
        rcount=0
        for (bcode,bname,bauthname,bprice,publ,qty,dop) in mycursor:
            rcount+=1
            print("==============================================")
            print("Book Code: ",bcode)
            print("Book Name: ",bname)
            print("Author of Book: ",bauthname)
            print("Price of Book: ",bprice)
            print("Publisher: ",publ)
            print("Total Quantity in Hand: ",qty)
            print("Purchased on: ",dop)
            print("===============================================")
            if rcount%2==0:
                print(rcount,"Record(s) found")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Searched Successfully..........")

    except Exception as ex:
        print(err)
        
    mydb.close()





def DisplayRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        sql="select * from bookrecords"
        mycursor.execute(sql)
        for (bcode,bname,bauthname,bprice,publ,qty,dop) in mycursor:
            print("==============================================")
            print("Book Code: ",bcode)
            print("Book Name: ",bname)
            print("Author of Book: ",bauthname)
            print("Price of Book: ",bprice)
            print("Publisher: ",publ)
            print("Total Quantity in Hand: ",qty)
            print("Purchased on: ",dop)
            print("===============================================")
        
        mydb.commit()
        mycursor.close()
        mydb.close()

    except Exception as ex:
        print(err)
        
    mydb.close()








def UpdateRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code of Book to be Updated from the Library: ")
        sql="select * from bookrecords where bookcode=%s"
        val=(bcode,)
        print("Enter New Record............")
        bname=input("Enter Book Name: ")
        bauthname=input("Enter Book Author's Name: ")
        bprice=int(input("Enter Book Price: "))
        publ=input("Enter Publisher of Book: ")
        qty=int(input("Enter Quantity Purchased: "))
        print("Enter Date of Purchase (Date/Month and year separately:)")
        DD=int(input("Enter Date: "))
        MM=int(input("Enter Month: "))
        YY=int(input("Enter Year: "))
        sql2="update bookrecords set bookname=%s,bookauthorname=%s,bookprice=%s,publisher=%s,quantity=%s,dop=%s where bookcode=%s"
        val2=(bname,bauthname,bprice,publ,qty,date(YY,MM,DD),bcode)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Updated Successfully..........")

    except Exception as ex:
        print(err)
        
    mydb.close()















