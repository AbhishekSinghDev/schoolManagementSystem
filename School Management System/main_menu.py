# import main_menu
import admission
import student_data
import fee_details
import lib_details
import mysql.connector as co
#import LOCK

#print(LOCK.login())

def run():
    while True:
        print("\t\t--------------------------------------------------------------------------------------")
        print("\t\t",' WELCOME TO SCHOOL MANAGEMENT SYSTEM ')
        print("\t\t--------------------------------------------------------------------------------------")
        print("\t\t     REMAL PUBLIC SCHOOL MAIN MENU")
        print("1. Admission")
        print("2. Student Data")
        print("3. Fee Details")
        print("4. Library Details")
        print("5. Exit")
        print("\t\t--------------------------------------------------------------------------------------")
        choice=int(input("Enter Your Choice : "))
    
        if choice == 1:
            admission.ADM_MENU()
        elif choice == 2:
            student_data.STU_MENU()
        elif choice == 3:
            fee_details.FEE_MENU()
        elif choice == 4:
            lib_details.LIB_MENU()
        elif choice == 5:
            print('THANK YOU FOR USING OUR PROGRAMM')
            break
        else:
            print("ERROR : INVALID CHOICE TRY AGAIN..... ")
            conti=input("PRESS ANY KEY TO CONTINUE..... ")

run()
int(input(" "))