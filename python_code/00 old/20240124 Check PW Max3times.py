def check_password():
    max_attempts = 3
    for attempts in range(1, max_attempts + 1):
        enter_password = input("Enter the password:")
        if enter_password == "ilovepython":
            print("Password OK")
            break
        if enter_password != "ilovepython":
            print("Wrong password")
            if attempts < max_attempts:
                print("Try it again")
            else:
                print("You enter too many times!")
                break
check_password()


