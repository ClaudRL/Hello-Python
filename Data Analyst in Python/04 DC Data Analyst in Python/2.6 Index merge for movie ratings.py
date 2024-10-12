# Index merge for movie ratings
# To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings. Ensure that your merge returns all rows from the movies table, and only matching rows from the ratings table.

# The movies and ratings tables have been loaded for you.

# Instructions
# 100 XP
# Merge the movies and ratings tables on the id column, keeping all rows from the movies table, and save the result as movies_ratings.

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on = 'id', how = 'left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())