# Your code here
def developers_cafe(espresso_quantity, cappucino_quantity, latte_quantity):
    espresso_price = 1.5
    calu_espresso_price = espresso_price * espresso_quantity
    cappucino_price = 2.75
    calu_cappucino_price = cappucino_price * cappucino_quantity
    latte_price = 3.25
    calu_latte_price = latte_price * latte_quantity

    print("Developers Cafe")
    print("----------------")
    print(f"{espresso_quantity}x Espresso (${espresso_price}) --- ${calu_espresso_price}")
    print(f"{cappucino_quantity}x Cappucino (${cappucino_price}) --- ${calu_cappucino_price}")
    print(f"{latte_quantity}x Latte (${latte_price}) --- ${calu_latte_price}")
    print("----------------")
    print(f"Total --- ${calu_espresso_price + calu_cappucino_price + calu_latte_price}")
developers_cafe(2,1,3)   
print（dia