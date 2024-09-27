def developers_cafe():
    # Get input for quantities
    espresso_quantity = int(input("Enter the quantity of Espresso: "))
    cappucino_quantity = int(input("Enter the quantity of Cappucino: "))
    latte_quantity = int(input("Enter the quantity of Latte: "))

    # Define prices
    espresso_price = 1.5
    cappucino_price = 2.75
    latte_price = 3.25

    # Calculate prices
    calu_espresso_price = espresso_price * espresso_quantity
    calu_cappucino_price = cappucino_price * cappucino_quantity
    calu_latte_price = latte_price * latte_quantity

    # Print receipt
    print("Developers Cafe")
    print("----------------")
    print(f"{espresso_quantity}x Espresso (${espresso_price}) --- ${calu_espresso_price}")
    print(f"{cappucino_quantity}x Cappucino (${cappucino_price}) --- ${calu_cappucino_price}")
    print(f"{latte_quantity}x Latte (${latte_price}) --- ${calu_latte_price}")
    print("----------------")
    print(f"Total --- ${calu_espresso_price + calu_cappucino_price + calu_latte_price}")

# Call the function to run the program
developers_cafe()
