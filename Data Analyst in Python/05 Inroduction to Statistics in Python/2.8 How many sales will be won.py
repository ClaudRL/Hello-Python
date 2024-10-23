# Exercise
# How many sales will be won?
# Now Amir wants to know how many deals he can expect to close each week if his 
# win rate changes. Luckily, you can use your binomial distribution knowledge to 
# help him calculate the expected value in different situations. Recall from the 
# video that the expected value of a binomial distribution can be calculated by n*p
# expected value = n * p

# Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 *0.35
print(won_35pct)


### Binomial Distribution and Expected Value Summary

In the context of binomial distribution, the **expected value (mean)** represents the average number of successes (in this case, won sales) you can expect based on the number of trials and the probability of success for each trial.

#### Formula for Expected Value:
- The expected value \( E(X) \) of a binomial distribution can be calculated as:
  \[
  E(X) = n \times p
  \]
  where:
  - \( n \) is the number of trials (e.g., number of sales attempts per week),
  - \( p \) is the probability of success on each trial (e.g., win rate).

#### In This Example:
- Amir works on **3 deals each week** (\( n = 3 \)).
- The **win rate** \( p \) changes between 25%, 30%, and 35%.

#### Calculations:
1. **Expected Sales with 30% Win Rate:**
   \[
   \text{won\_30pct} = 3 \times 0.30 = 0.9
   \]
   Amir can expect to win **0.9 deals per week** if his win rate is 30%.

2. **Expected Sales with 25% Win Rate:**
   \[
   \text{won\_25pct} = 3 \times 0.25 = 0.75
   \]
   Amir can expect to win **0.75 deals per week** if his win rate drops to 25%.

3. **Expected Sales with 35% Win Rate:**
   \[
   \text{won\_35pct} = 3 \times 0.35 = 1.05
   \]
   Amir can expect to win **1.05 deals per week** if his win rate rises to 35%.

### Summary:
- The expected value allows us to predict the **average** number of successes (or deals won) given a certain probability and number of trials.
- By adjusting the win rate \( p \), we can see how Amir’s expected weekly deals change:
  - At a **30% win rate**, Amir expects **0.9 deals**.
  - At a **25% win rate**, Amir expects **0.75 deals**.
  - At a **35% win rate**, Amir expects **1.05 deals**.
