def login():
    uname = input("ENTER USERNAME : ")
    passw = input("ENTER PASSWORD : ")

    if (uname == "admin" and passw == "2580"):
        import main_menu as m
        m.run()
    else:
        print("ACCESS DENIED!!!")
        conti=input("PRESS ANY KEY TO CONTINUE")
        login()

login()
