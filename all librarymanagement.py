

#Python Module:Library Management


import menulib
import book
import member
import issue


while True:
    print("\t\t******Library Management******\n")
    print("==========================================")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue/Return Book")
    print("4. Exit")
    print("==========================================")
    choice=int(input("Enter choice between 1 to 4 -------> :"))
    if choice==1:
        menulib.MenuBook()
    elif choice==2:
        menulib.MenuMember()
    elif choice==3:
        menulib.MenuIssueReturn()
    elif choice==4:
        break
    else:
        print("Wrong choice.......Enter your choice again")
        x=input("enter any key to continue")


#Python Module: Menulib

import book
import member
import issue


def MenuBook():
    while True:
        print("\t\t*****Book Record Management*****\n")
        print("=====================================")
        print("1. Add Book Records")
        print("2. Display Book Records")
        print("3. Search Book Records")
        print("4. Delete Book Records")
        print("5. Update Book Records")
        print("6. Return to Main Menu")
        print("======================================")
        choice=int(input("Enter choice between 1 to 5-------->: "))
        if choice==1:
            book.AddRecords()
        elif choice==2:
            book.DisplayRecords()
        elif choice==3:
            book.SearchRecords()
        elif choice==4:
            book.DeleteRecords()
        elif choice==5:
            book.UpdateRecords()
        elif choice==6:
            return
        else:
            print("Wrong choice.......Enter your choice again")
            x=input("Enter any key to continue")


def MenuMember():
    while True:
        print("\t\t*****Member Record Management*****\n")
        print("=====================================")
        print("1. Add Member Records")
        print("2. Display Member Records")
        print("3. Search Member Records")
        print("4. Delete Member Records")
        print("5. Update Member Records")
        print("6. Return to Main Menu")
        print("======================================")
        choice=int(input("Enter choice between 1 to 5-------->: "))
        if choice==1:
            member.AddMember()
        elif choice==2:
            member.DisplayMember()
        elif choice==3:
            member.SearchMember()
        elif choice==4:
            member.DeleteMember()
        elif choice==5:
            member.UpdateMember()
        elif choice==6:
            return
        else:
            print("Wrong choice.......Enter your choice again")
            x=input("Enter any key to continue")


def MenuIssueReturn():
    while True:
        print("\t\t*****Member Record Management*****\n")
        print("=====================================")
        print("1. Issue Book")
        print("2. Display Issued Book Records")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("======================================")
        choice=int(input("Enter choice between 1 to 4-------->: "))
        if choice==1:
            issue.IssueBook()
        elif choice==2:
            issue.DisplayIssuedBook()
        elif choice==3:
            issue.ReturnBook()
        elif choice==4:
            return
        else:
            print("Wrong choice.......Enter your choice again")
            x=input("Enter any key to continue")


#Python Module: Book

from mysql.connector import errorcode
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()


def UpdateRecords():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        bcode=input("Enter Book Code of Book to be Updated from the Library: ")
        sql="select * from bookrecords where bookcode=%s"
        val=(bcode,)
        print("Enter New Record")
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()

#Python Module: Member

from mysql.connector import errorcode
from datetime import date,datetime,timedelta
import mysql.connector

def AddMember():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        mcode=input("Enter Member Code: ")
        mname=input("Enter Member Name: ")
        mmob=input("Enter Member's Mobile Number: ")
        print("Enter Date of Membership (Date/Month and year separately:)")
        DD=int(input("Enter Date: "))
        MM=int(input("Enter Month: "))
        YY=int(input("Enter Year: "))
        madd=input("Enter Member's Address: ")
        sql="insert into memberrecords values(%s,%s,%s,%s,%s)"
        val=(mcode,mname,mmob,date(YY,MM,DD),madd)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Inserted Successfully..........")

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()

def DeleteMember():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        mcode=input("Enter Member Code to be Deleted from the Library: ")
        sql="delete from memberrecords where memberno=%s"
        val=(mcode,)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Deleted Successfully..........")

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()


def SearchMember():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        mcode=input("Enter Member Code to be Searched from the Library: ")
        sql="select * from memberrecords where memberno=%s"
        val=(mcode,)
        mycursor.execute(sql,val)
        rcount=0
        for (mcode,mname,mmob,dom,madd) in mycursor:
            rcount+=1
            print("==============================================")
            print("Member Code: ",mcode)
            print("Member Name: ",mname)
            print("Mobile Number of Member: ",mmob)
            print("Date of membership: ",dom)
            print("Address of Member: ",madd)
            print("===============================================")
            if rcount%2==0:
                print(rcount,"Record(s) found")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Searched Successfully..........")

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()


def DisplayMember():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        sql="select * from memberrecords"
        mycursor.execute(sql)
        for (mcode,mname,mmob,dom,madd) in mycursor:
            print("==============================================")
            print("Member Code: ",mcode)
            print("Member Name: ",mname)
            print("Mobile Number of Member: ",mmob)
            print("Date of membership: ",dom)
            print("Address of Member: ",madd)
            print("===============================================")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Displayed Successfully..........")

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()


def UpdateMember():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
        mycursor=mydb.cursor()
        mcode=input("Enter Member Code to be Updated from the Library: ")
        sql="select * from memberrecords where memberno=%s"
        val=(mcode,)
        print("Enter New Record")
        mname=input("Enter Member Name: ")
        mmob=input("Enter Mobile Number of Member: ")
        print("Enter Date of Membership (Date/Month and year separately:)")
        DD=int(input("Enter Date: "))
        MM=int(input("Enter Month: "))
        YY=int(input("Enter Year: "))
        madd=input("Enter Address of Member: ")
        sql2="update memberrecords set mname=%s,mmobile=%s,dom=%s,maddress=%s where memberno=%s"
        val2=(mname,mmob,date(YY,MM,DD),madd,mcode)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Updated Successfully..........")

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()


#Python Module: Issue


from mysql.connector import errorcode
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
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

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database Doesn't Exist")
        else:
            print(err)
    mydb.close()








