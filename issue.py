


#Python Module: Issue


from datetime import date,datetime,timedelta
import mysql.connector



def IssueBook():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code to issue: ")
        mcode=input("Enter Member Code: ")
        print("Enter Date of Issue (Date/Month and year separately:)")
        DD=int(input("Enter Date: "))
        MM=int(input("Enter Month: "))
        YY=int(input("Enter Year: "))
        sql="insert into issuebooks(bookcode,memberno,doi) values (%s,%s,%s)"
        val=(bcode,mcode,date(YY,MM,DD))
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Inserted Successfully..........")

    except Exception as ex:
        print(err)
        
    mydb.close()







def ReturnBook():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code of Book to be Returned to the Library: ")
        mcode=input("Enter Member Code of Member who is returning Book: ")
        dor=date.today()
        sql2="update issuebooks set dor=%s where bookcode=%s and memberno=%s"
        val2=(dor,bcode,mcode)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Deleted Successfully..........")

    except Exception as ex:
        print(err)
        
    mydb.close()







def DisplayIssuedBook():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        sql="select B.bookcode,B.bookname,M.memberno,M.mname,I.doi,I.dor from bookrecords B,issuebooks I,memberrecords M where B.bookcode=I.bookcode and I.memberno=M.memberno"
        mycursor.execute(sql)
        for (bcode,bname,mcode,mname,doi,dor) in mycursor:
            print("==============================================")
            print("Book Code: ",bcode)
            print("Book Name: ",bname)
            print("Member Code: ",mcode)
            print("Member Name: ",mname)
            print("Date of Issue: ",doi)
            print("Date of Return: ",dor)
            print("===============================================")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("I Have done It.......................")

    except Exception as ex:
        print(err)
        
    mydb.close()









