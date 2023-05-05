import main_menu
import lib_details
import mysql.connector as co

def LIB_MENU():
    while True:
        print("\t\t-------------------------------------")
        print('\t\t WELCOME TO SCHOOL MANAGEMENT SYSTEM ')
        print("\t\t-------------------------------------")
        print("\t\t\t LIBRARY MENU ")
        print("1. Add book ")
        print("2. Search Book ")
        print("3. Delete Book")
        print("4. Book Issue")
        print("5. Show All Records")
        print("6. Return to Main Menu ")
        print("\t\t----------------------------------")
        choice=int(input("Enter Your Choice [1-6]-----|  "))

    

        if choice == 1:
            lib_details.book_addbook()
        elif choice == 2:
            lib_details.book_schbook()
        elif choice == 3:
            lib_details.book_delbook()
        elif choice == 4:
            lib_details.book_bkissue()
        elif choice == 5:
            lib_details.book_show_records()
        elif choice == 6:
            return
        else:
            print("ERROR : INVALID CHOICE TRY AGAIN..... ")
            conti=input("PRESS ANY KEY TO CONTINUE..... ")

def book_addbook():
    try:
        mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
        cursor=mycon.cursor()
        bk_id=input("Enter book id : ")
        bk_name=input("Enter Book name : ")
        bk_author=input("Enter author of book : ")
        bk_publisher=input("Enter Publisher of book : ")
        issued_to=input("Enter details book to be issued (if NO then enter null): ")

        query="insert into lib_details(bk_id,bk_name,bk_author,bk_publisher,issued_to)values('{}','{}','{}','{}','{}')".format(bk_id,bk_name,bk_author,bk_publisher,issued_to)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved sucessfully')
    except:
        print('error')

def book_schbook():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ad=input("Enter book id : ")
    st="select * from lib_details where bk_id='%s'"%(ad)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)
def book_delbook():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ad=input("Enter book id : ")
    st="delete from lib_details where bk_id='%s'"%(ad)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted sucessfully")
def book_bkissue():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter book id : ")
    cn=input("Enter details of person book to be issued : ")
    st="update lib_details set issued_to='%s' where bk_id='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Book issued successfully")

def book_show_records():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    cursor.execute("select * from lib_details")
    data=cursor.fetchall()
    for row in data:
        print(row)



    
