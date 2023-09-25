

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
    print("4. Database Setup")
    print("5. Exit")
    print("==========================================")
    choice=int(input("Enter choice between 1 to 4 -------> :"))
    if choice==1:
        menulib.MenuBook()
    elif choice==2:
        menulib.MenuMember()
    elif choice==3:
        menulib.MenuIssueReturn()
    elif choice==4:
        menulib.DataBase()
    elif choice==5:
        break
    else:
        print("Wrong choice.......Enter your choice again")
        x=input("enter any key to continue")
