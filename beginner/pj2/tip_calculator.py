print("Welcome to the tip calculator!")
t_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))

cost = (t_bill / num_of_people) * (1 + tip/100)

print(f"Each person should pay: ${cost:.2f}")