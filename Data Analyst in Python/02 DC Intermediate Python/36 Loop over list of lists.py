# Exercise
# Loop over list of lists
# Remember the house variable from the Intro to Python course? Have a look at its definition in the script. It's basically a list of lists, where each sublist contains the name and area of a room in your house.

# It's up to you to build a for loop from scratch this time!

# Instructions
# 100 XP
# # Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.

# house list of lists
house = [["hallway", 11.25, "small"], 
         ["kitchen", 18.0,"big"], 
         ["living room", 20.0, "big"], 
         ["bedroom", 10.75, "small"], 
         ["bathroom", 9.50, "small"]]
         
# Build a for loop from scratch
for x , y , z in house:
    print(f"the {x} is {y} sqm")
    print(f"It's a {z} room")