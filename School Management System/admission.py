
import main_menu
import mysql.connector as co

def ADM_MENU():
    while True:
        print("\t\t--------------------------------------")
        print('\t\t WELCOME TO SCHOOL MANAGEMENT SYSTEM ')
        print("\t\t--------------------------------------")
        print("\t\t\t ADMISSION MENU  ")
        print("1. Add Admission Detais")
        print("2. Show Asmission Details")
        print("3. Seacrh ")
        print("4. Update Admission Details")
        print("5. Delete Admissoion Details")
        print("6. Return to Main Menu...")
        print("\t\t----------------------------------")
        choice=int(input("Enter Your Choice [1-6]-----|  "))

        if choice == 1:
            admin_detls()
        elif choice == 2:
            show_admin_details()
        elif choice == 3:
            search_admin_details()
        elif choice == 4:
            edit_admin_details()
        elif choice == 5:
            del_admin_details()
        elif choice ==6:
            return
        else:
            print("ERROR : INVALID CHOICE TRY AGAIN..... ")
            conti=input("PRESS ANY KEY TO CONTINUE..... ")

def admin_detls():
    try:
        mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
        cursor=mycon.cursor()
        adno=input("Enter admission number: ")
        rno=int(input("Enter the roll no. : "))
        sname=input("Enter the student name : ")
        address=input("Enter the address : ")
        phno=input("Enter the phone number : ")
        clas=input("Enter class : ")

        query="insert into admission(adno,rno,sname,address,phno,class)values('{}',{},'{}','{}','{}','{}')".format(adno,rno,sname,address,phno,clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')
    except:
        print('error')

def show_admin_details():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    cursor.execute("select * from admission")
    data=cursor.fetchall()
    for row in data:
        print(row)
def search_admin_details():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ad=input("Enter Admission Number : ")
    st="select * from admission where adno='%s'"%(ad)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)


def edit_admin_details():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage"))
    cursor=mycon.cursor()

    print("1.Edit Name ")
    print("2.Edit Address ")
    print("3.Phone number ")
    print("4.Return ")
    print("\t\t------------------------------------")
    choice=int(input("Enter your choice : "))
    if choice==1:
        admission.edit_name()
    elif choice ==2:
        admission.edit_address()
    elif choice==3:
        admission.edit_phno()
    elif choice==4:
        return
    else:
        print("Error invalid choice try again.....")
        conti="Press any key to return to "

def edit_name():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input('Enter Admission no : ')
    cn=input("Enter the correct name : ")
    st="update admission set sname='%s' where adno='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updates successfully")
def edit_address():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Admission no : ")
    cn=input("Enter the correct address : ")
    st="update admission set address='%s' where adno='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Address updated successfully ")
def edit_phno():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Admission no : ")
    cn=input("Enter the correct phone no : ")
    st="update admission set phno='%s' where adno='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Phone number updated sucessfully")

def del_admin_details():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Admission no. : ")
    st="delete from admission where adno='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted sucessfully")

        
