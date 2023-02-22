# ## Tip Calculator

# # Instructions

# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# # Example Input

# ```
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# ```

# # Example Output

# ```
# Each person should pay: $19.93
# ```


# # Hint

# 1. [How to round a number to 2 decimal places in Python](https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal)
# 2. [How to limit a float to two decimal places in Python](https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python)


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
number_of_people = float(input("How many people in your party? "))
tip = (float(input("How much would you like to tip? ")))/100

split_bill = round((bill) / number_of_people, 2)
split_tip = round((tip) / number_of_people, 2)
total_split = round(split_tip + split_bill, 2)


print(f"Thus everyone's share of the total bill is ${split_bill} plus a {split_tip}")
print(f"Each person should pay: {total_split}")