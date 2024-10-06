# Write a program that repeatedly prompts a user 
# for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything 
# other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the 
# number. Enter 7, 2, bob, 10, and 4 and match the 
# output below.

largest = None # None 即为空值，这里很关键，能解决largest, smallest首次赋值的问题。
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    try:
        number = int(num)
        
        if largest is None or number > largest: # or 的运算从左往右。
        # if number > largest or largest is None : # 就会报错
            largest = number
        
        if smallest is None or number < smallest:
            smallest = number
    
    except ValueError:
        print("Invalid input")

if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers were entered.")