import main_menu
import admission
import mysql.connector as co
import student_data
def STU_MENU():
    while True:
        print("\t\t--------------------------------------")
        print('\t\t WELCOME TO SCHOOL MANAGEMENT SYSTEM ')
        print("\t\t--------------------------------------")
        print("\t\t\t STUDENT DATA MENU ")
        print("1. Add Student Record ")
        print("2. Show all Admission Details ")
        print("3. Search Sutdent Record ")
        print("4. Delete Student Record")
        print("5. Update Student Record")
        print("6. Exit")
        print("\t\t----------------------------------")
        choice=int(input("Enter Your Choice [1-6]-----|  "))

        if choice == 1:
            student_data.ADD_Records()
        elif choice == 2:
            student_data.SHOW_STU_DETAILS()
        elif choice == 3:
            student_data.SEARCH_STU_DETAILS()
        elif choice == 4:
            student_data.DELETE_STU_DETAILS()
        elif choice == 5:
            student_data.EDIT_STU_DETAILS()
        elif choice == 6:
            return
        else:
            print("ERROR : INVALID CHOICE TRY AGAIN..... ")
            conti=input("PRESS ANY KEY TO CONTINUE..... ")


def ADD_Records():
    try:
        mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
        cursor=mycon.cursor()
        session=int(input("Enter academic session(eg,2019-20) : "))
        stname=input("Enter student name : ")
        stclass=input("Enter class : ")
        stsec=input("Enter section : ")
        stroll=int(input("Enter roll no : "))
        sub1=input("Enter subject 1 : ")
        sub2=input("Enter subject 2 : ")
        sub3=input("Enter subject 3 : ")

        query="insert into student_data(session,stname,stclass,stsec,stroll,sub1,sub2,sub3)values({},'{}','{}','{}',{},'{}','{}','{}')".format(session,stname,stclass,stsec,stroll,sub1,sub2,sub3)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in student table")
    except:
        print("error")

def SHOW_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    cursor.execute("select * from student_data")
    data=cursor.fetchall()
    for row in data:
        print(row)

def SEARCH_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no. : ")
    st="select * from student_data where stroll='%s'"%(ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)
def DELETE_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no. : ")
    st="delete from student_data where stroll='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted sucessfully")
def EDIT_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    print('1.Edit session : ')
    print('2.Edit name : ')
    print('3.Edit class : ')
    print('4.Edit section : ')
    print('5.Edit Roll no : ')
    print('6.Edit sub1 : ')
    print('7.Edit sub2 : ')
    print('8.Edit sub3 : ')
    print('9.Return')
    print("\t\t---------------------------------------")
    choice=int(input("Enter your choice : "))
    if choice==1:
        student_data.editsession()
    elif choice==2:
        student_data.editname()
    elif choice==3:
        student_data.editclass()
    elif choice==4:
        student_data.editsection()
    elif choice==5:
        student_data.editroll()
    elif choice==6:
        student_data.editsub1()
    elif choice==7:
        student_data.editsub2()
    elif choice==8:
        student_data.editsub3()
    elif choice==9:
        return
    else:
        print("INVALID CHOICE................")

def editsession():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter roll no. : ")
    cn=input("Enter correct session : ")
    st="update student_data set session='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Session Updated sucessfully")
def editname():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter roll no . : ")
    cn=input("Enter the correct name : ")
    st="update student_data set stname='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Student Name updates sucessfully")
def editclass():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct class no : ")
    st="update student_data set stclass='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Student name updated sucessfully")
def editsection():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct section : ")
    st="update student_data set stsec='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Section updated sucessfully")
def editroll():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct roll no. : ")
    st="update student_data set stroll='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Roll number = updated sucessfully")
def editsub1():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct subject1 : ")
    st="update student_data set sub1='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Subject1 updated sucessfully")
def editsub2():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct subject2 : ")
    st="update student_data set sub2='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Subject2 updated sucessfully")
def editsub3():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    ac=input("Enter Roll no : ")
    cn=input("Enter the correct subject3 : ")
    st="update student_data set sub3='%s' where stroll='%s'"%(cn,ac)
    cursor.execute(st)
    mycon.commit()
    print("Subject3 updated sucessfully")
