import main_menu
import fee_details
import mysql.connector as co

def FEE_MENU():
    while True:
        print("\t\t---------------------------------------")
        print('\t\t  WELCOME TO SCHOOL MANAGEMENT SYSTEM ')
        print("\t\t---------------------------------------")
        print("\t\t\t STUDENT MENU ")
        print("1. Fee Deposit")
        print("2. Fee Details")
        print("3. Return to main menu..")
        print("\t\t----------------------------------")
        choice=int(input("Enter Your Choice [1-3]----|  "))

        if choice == 1:
            fee_details.fee_deposit()
        elif choice == 2:
            fee_details.fee_det()
        elif choice == 3:
            return
        else:
            print("ERROR : INVALID CHOICE TRY AGAIN..... ")
            conti=input("PRESS ANY KEY TO MAIN MENU..... ")


    
def fee_deposit():
    try:
        mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
        cursor=mycon.cursor()
        stroll=input("Enter roll no. : ")
        stname=input("Enter student name : ")
        print("NOTE : YOU CAN  ONLY DEPOSIT FEES OF CLASS X AND XII (enter class in capital letter)")
        stclass=input("Enter student class eg(X/XII): ")
        if stclass=='X':
            print("Total fees (annually)= 36000")
        elif stclass=='XII':
            print("Total fees (annually)= 48000")
        else:
            print("You have not followed the NOTE")
            print("Press any key to retry")
            return
            
        stfee=int(input("Enter amount you want to submit  : "))
        
        if stfee >36000:
            print('you have entered the excess amount now go all the money is ours!!')
        elif stfee >48000:
            print('you have entered the excess amount now go all the money is ours!!')

        query="insert into fee_details(stroll,stname,stclass,stfee)values('{}','{}','{}',{})".format(stroll,stname,stclass,stfee)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Fees deposited successfully")
    except:
        print("error")
def fee_det():
    mycon=co.connect(host="localhost",user="root",password="remal25",charset='utf8',database="schmanage")
    cursor=mycon.cursor()
    cursor.execute("select * from fee_details")
    data=cursor.fetchall()
    for row in data:
        print(row)
