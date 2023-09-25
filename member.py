

#Python Module: Member


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

    except Exception as ex:
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

    except Exception as ex:
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

    except Exception as ex:
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

    except Exception as ex:
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

    except Exception as ex:
        print(err)
        
    mydb.close()






