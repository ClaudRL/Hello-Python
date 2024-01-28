# Odd or even number
while True:
    user_enter = input("Enter a number (or 'ok' to quit): ")

    if user_enter.lower() == 'ok':
        print("Exiting the program.")
        break

    try:
        num = int(user_enter)
        if num == 0:
            print("Zero")
        else:
            even_num = num % 2
            if even_num == 0:
                print("Even number")
            else:
                print("Odd number")
    except ValueError:
        print("Invalid input. Please enter a number or 'ok' to quit.")