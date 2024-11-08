import numpy as np

"""
TASK 2.3
What is the probability that sum of three dice will exceed 6?
"""
num_simulations = 10 # počet simulací
rolls = np.random.randint(1, 7, (num_simulations, 3))

print(rolls)
sums = rolls.sum(axis=1)
pravdepodobnost = np.mean(sums > 6) # chci aby součet byl vyšší než 6
print(f"Pravděpodobnost: {pravdepodobnost:.4f}")


"""
TASK 2.4
What is the probability that half the product of three dice will exceed their sum?
"""
num_simulations = 10 # počet simulací
rolls = np.random.randint(1, 7, (num_simulations, 3))

print(rolls)

multipl = np.prod(rolls, axis=1)/2
sums = rolls.sum(axis=1)
pravdepodobnost = np.mean(multipl>sums)
print(f"Pravděpodobnost: {pravdepodobnost:.4f}")

"""
TASK 2.5
Each of two possible outcomes of an experiment has an equal likelihood of occuring, ie.  P(H)=P(T)=12. 

Perform a trial by flipping a virtual coin  n  times, where  n∈{10,100,1000,1000000} , and count how many times we get heads. 
See, if the expected number of heads is equal to the number you get in each trial. 
Which results are the closest to the ideal number?
"""

trials = [10, 100, 1000, 1000000]

for n in trials:
    flips = np.random.choice(['H', 'T'], size=n)
    heads_count = np.sum(flips == 'H')
    print(f"{n} pokusů, hlava padla {heads_count}x, pravděpodobnost: {heads_count/n:.4f}")

"""
TASK 2.6 Roll a dice
Perform the exact same experiment as in Task 2.5 with rolling a fair six-sided dice with the following sides  {1,2,2,3,3,3} . 
What are the number you get the most?
"""

dice = [1, 2, 2, 3, 3, 3]
trials = [10, 100, 1000, 1000000]

for n in trials:
    rolls = np.random.choice(dice, size=n)
    #print(rolls)
    counts = {1: 0, 2: 0, 3: 0}
    for roll in rolls:
        counts[roll] += 1
    
    most_common_number = max(counts, key=counts.get)
    most_common_count = counts[most_common_number]
    ratio = most_common_count / n
    print(f"Pro {n} hodů, nejčastěji padlo číslo {most_common_number}  {most_common_count}x, pravděpodobnost: {ratio:.4f}")
    
