def valid_email(email):
    if "@" not in email or "." not in email:
        print("Invalid email")
    else:
        # Get username
        username = email.split("@")[0]
        
        # check username length
        def check_username_length(username):
            if len(username) >= 5:
                print("Valid Email")
            else:
                print("Invalid email: Username should be at least 5 characters long")

        check_username_length(username)

valid_email("asd@ksasig.com")
