user_enter = input("Enter a number: ")

num = int(user_enter)

if num == 0:
  print("Zero")
else:
  even_num = num % 2
  if even_num == 0:
    print("even number")
  else:
    print("odd number")