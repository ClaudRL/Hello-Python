# Exercise
# Indexes and values (2)
# For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?

# Instructions
# 100 XP
# Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas,1) :
    print("room " + str(index) + ": " + str(area))