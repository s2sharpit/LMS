

#Python Module: Menulib

import book
import member
import issue
import MyDatabase



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




def DataBase():
    while True:
        print("\t\t*****Database Management*****\n")
        print("=====================================")
        print("1. Database Creation")
        print("2. Creation of Relations")
        print("3. List of Relations")
        print("4. Return to Main Menu")
        print("======================================")
        choice=int(input("Enter choice between 1 to 4-------->: "))
        if choice==1:
            MyDatabase.CreateDatabase()
        elif choice==2:
            MyDatabase.CreateRelations()
        elif choice==3:
            MyDatabase.ShowRelations()
        elif choice==4:
            return
        else:
            print("Wrong choice.......Enter your choice again")
            x=input("Enter any key to continue")

