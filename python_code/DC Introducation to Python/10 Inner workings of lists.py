# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#If you want to prevent changes in areas_copy 
# from also taking effect in areas, you'll have
#  to do a more explicit copy of the areas list 
# with list() or by using [:].
# Change this command
areas_copy = areas[:]


# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)