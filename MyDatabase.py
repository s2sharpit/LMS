
#Python Module: MyDatabase


#from datetime import date,datetime,timedelta
import mysql.connector



def CreateDatabase():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root")
              mycursor=mydb.cursor()
              print("Creating Library Database")
              sql="create database if not exists LIBRARY"
              mycursor.execute(sql)
              print("LIBRARY Database Created Successfully....")
              
       except Exception as ex:
              print(ex)
       


def CreateRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Library")
              mycursor=mydb.cursor()
              print("Creating bookrecords Relation")
              sql="create table if not exists bookrecords(bookcode int primary key,bookname varchar(50) not null,bookauthorname varchar(50) not null,bookprice int,publisher varchar(80) not null,quantity int,dop date)"
              mycursor.execute(sql)
              print("bookrecords Relation Created Successfully....")
              print("Creating memberrecords Relation")
              sql="create table if not exists memberrecords(memberno int primary key,mname varchar(60) not null,mmobile varchar(10) not null,dom date,maddress varchar(120))"
              mycursor.execute(sql)
              print("memberrecords Relation Created Successfully....")
              print("Creating issuebooks Relation")
              #sql="create table issuebooks(bookcode int references bookrecords(bookcode),memberno int references memberrecords(memberno),doi date,dor date)"
              sql="create table issuebooks(bookcode int, memberno int, doi date, dor date)"
              mycursor.execute(sql)
              sql="alter table issuebooks add FOREIGN KEY(bookcode) references bookrecords(bookcode), add FOREIGN KEY(memberno) references memberrecords(memberno)"
              mycursor.execute(sql)
              print("issuebooks Relation Created Successfully....")

       except Exception as ex:
              print(ex)


def ShowRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="LIBRARY")
              mycursor=mydb.cursor()
              print("Displaying List of Relations")
              sql="show tables"
              mycursor.execute(sql)
              for i in mycursor:
                     print(i)
             
              
       except Exception as ex:
              print(ex)

       




