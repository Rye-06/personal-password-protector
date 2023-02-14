# This program asks for authentication by one of the two methods- Phone or Email

# Asks would you want to authenticate:
ask_check = False
while ask_check == False:
    ask = input("Would you like to login into your account?")
    if ask == "Yes":
        print("Okay! Let's get right into it.")
        ask_check = True

    elif ask == "No":
        print("Sure. No problem! See you next time.")
        ask_check = False
        exit()

    else:
        print("Please say YES or NO.")
        ask_check = False

# Asks how you want to authenticate:
how = input("How would you like to have the code be sent to you?")
check_1 = False
while check_1 == False:
    # Email code start:
    if how == "Email":
        print("Sure!")
        check_1 = True
        check_2 = False
        while check_2 == False:
            email_check = input(
                "Please enter your email so we can send a confirmation mail:")
            gmail = "@gmail.com"
            email_len = len(email_check)
            # for gmail in email_check :
            if gmail in email_check and email_len > 10:
                print("Thanks! Check your mail for the authentication code!")
# Authenticate code EMAIL start:
                authentication_code = 1234
                check_3 = False
                while check_3 == False:
                    authentication_code = int(
                        input("Enter the code to unlock your account:"))
                    if authentication_code == 1234:
                        print("Perfect! You can now access your account.")
                        check_3 = True
                    elif authentication_code != 1234:
                        print("Sorry. Your authentication code is wrong!")
                        check_3 = False
# Authenticate code EMAIL end here
                check_2 = True
                break
            else:
                print("Oh! That is not a valid email address. Please renter the email.")
                check_2 == False
# Email code end here
# Phone code start:
    elif how == "Phone":
        print("Sure!")
        check_1 = True
        check_4 = False
        while check_4 == False:
            the_number = input("Please enter your phone number:")
            string_Number = str(the_number)
            number_Length = len(string_Number)
            if number_Length == 11:
                print("Check your phone, we have sent you an OTP.")
                check_4 = True
# Authenticate code PHONE start:
                authentication_code = 1234
                check_3 = False
                while check_3 == False:
                    authentication_code = int(
                        input("Enter the code to unlock your account:"))
                    if authentication_code == 1234:
                        print("Perfect! You can now access your account.")
                        check_3 = True
                    elif authentication_code != 1234:
                        print("Sorry. Your authentication code is wrong!")
                        check_3 = False
# Authenticate code PHONE end here
            else:
                print("Please enter a valid number.")
                check_4 == False
# Phone code end here

# CODE FINISHED
