def convert(money):
    if money[0] == "$":
        number = float(money[1:])
        to_euro = round((number/1.1),2)
        euro = "€" + str(to_euro)
        return euro
    if money[0] == "€":
        number = float(money[1:])
        to_usd = round((number)*1.1, 2)
        usd = "$" + str(to_usd)
        return usd
convert("€50")
