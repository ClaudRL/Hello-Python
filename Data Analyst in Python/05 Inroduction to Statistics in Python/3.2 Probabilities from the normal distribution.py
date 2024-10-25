# Probabilities from the normal distribution
# Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.

# norm from scipy.stats is imported as well as pandas as pd. The DataFrame amir_deals is loaded.

# 1. What's the probability of Amir closing a deal worth less than $7500?
# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

# print(prob_less_7500)

# 2. What's the probability of Amir closing a deal worth more than $1000?


# 3. What's the probability of Amir closing a deal worth between $3000 and $7000?


# 4. What amount will 25% of Amir's sales be less than?