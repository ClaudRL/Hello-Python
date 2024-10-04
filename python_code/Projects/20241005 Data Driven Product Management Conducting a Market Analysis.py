# # # https://projects.datacamp.com/projects/1684

# # Project Instructions
# # Help the fitness studio explore interest in workouts at a global and national level.

# # When was the global search for 'workout' at its peak? Save the year of peak interest as a string named year_str in the format "yyyy".

# # Of the keywords available, what was the most popular during the covid pandemic, and what is the most popular now? Save your answers as variables called peak_covid and current respectively.

# # What country has the highest interest for workouts among the following: United States, Australia, or Japan? Save your answer as top_country.

# # You'd be interested in expanding your virtual home workouts offering to either the Philippines or Malaysia. Which of the two countries has the highest interest in home workouts? Identify the country and save it as home_workout_geo.

# Last edit was 4 months ago
# gym

# You are a product manager for a fitness studio and are interested in understanding the current demand for digital fitness classes. You plan to conduct a market analysis in Python to gauge demand and identify potential areas for growth of digital products and services.

# The Data
# You are provided with a number of CSV files in the "Files/data" folder, which offer international and national-level data on Google Trends keyword searches related to fitness and related products.

# workout.csv
# Column	Description
# 'month'	Month when the data was measured.
# 'workout_worldwide'	Index representing the popularity of the keyword 'workout', on a scale of 0 to 100.
# three_keywords.csv
# Column	Description
# 'month'	Month when the data was measured.
# 'home_workout_worldwide'	Index representing the popularity of the keyword 'home workout', on a scale of 0 to 100.
# 'gym_workout_worldwide'	Index representing the popularity of the keyword 'gym workout', on a scale of 0 to 100.
# 'home_gym_worldwide'	Index representing the popularity of the keyword 'home gym', on a scale of 0 to 100.
# workout_geo.csv
# Column	Description
# 'country'	Country where the data was measured.
# 'workout_2018_2023'	Index representing the popularity of the keyword 'workout' during the 5 year period.
# three_keywords_geo.csv
# Column	Description
# 'country'	Country where the data was measured.
# 'home_workout_2018_2023'	Index representing the popularity of the keyword 'home workout' during the 5 year period.
# 'gym_workout_2018_2023'	Index representing the popularity of the keyword 'gym workout' during the 5 year period.
# 'home_gym_2018_2023'	Index representing the popularity of the keyword 'home gym' during the 5 year period.


# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Start coding here
# 1. Load data on global interest in workouts
df_workout = pd.read_csv("data/workout.csv")

# add year column
df_workout['month'] = pd.to_datetime(df_workout['month'])
df_workout['year'] = df_workout['month'].dt.year

# 2. Find the time of peak searches for workout
plt.figure(figsize=(16,10))
plt.plot(df_workout['month'],df_workout['workout_worldwide'])
plt.show()
# year_str = "2020"

# 3 Find the most popular keywords for the current year and during covid
df_3_keywords = pd.read_csv("data/three_keywords.csv")
df_3_keywords ['month'] = pd.to_datetime(df_3_keywords['month'])
# print(df_3_keywords.info())
plt.figure(figsize=(16,10))
plt.title("The most popular keywords")
plt.plot(df_3_keywords['month'],df_3_keywords['home_workout_worldwide'], color='red', label="Home workout")
plt.plot(df_3_keywords['month'],df_3_keywords['gym_workout_worldwide'], color='yellow', label="Gym workout")
plt.plot(df_3_keywords['month'],df_3_keywords['home_gym_worldwide'], color='blue', label="Home gym")
plt.legend()
plt.show()

peak_covid = "Home workout"
current = "Gym workout"

# 4 Find the country with the highest interest for workout
df_workout_geo = pd.read_csv("data/workout_geo.csv")
uaj_countries = ["United States", "Australia", "Japan"]
print(df_workout_geo[df_workout_geo['country'].isin(uaj_countries)])

top_country = "United States"

# 5 Find the country in the MESA region with the highest interest in home workouts
df_3_keywords_geo = pd.read_csv("data/three_keywords_geo.csv")
# print(df_3_keywords_geo.info())
mesa_countries = ["Philippines", "Malaysia"]
mesa_data = df_3_keywords_geo[df_3_keywords_geo['Country'].isin(mesa_countries)]
print(mesa_data[['Country', 'home_workout_2018_2023']].sort_values('home_workout_2018_2023', ascending=False))
# home_workout_geo = "Philippines"