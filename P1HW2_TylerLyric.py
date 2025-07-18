 # Lyric Tyler
 # June 16th, 2025
 # P1HW2
 # A small program that calculates and displays the total 

budget = int(input("Enter your preferred budget: "))
destination = input("What's your desired travel destination?: ")
gas = int(input("Enter the amount of money spent on gas: "))
accommodation = int(input("Enter the amount of money spent on accommodations: "))
food = int(input("Enter the amount of money spent on food: "))

expenses = budget + gas + accommodation + food
remaining_balance = expenses - budget

location = destination
intial_budget = budget

print("--------Travel Expenses--------")
print("Location: ", location)
print("Intial budget: ", intial_budget)

print("Fuel: ", gas)
print("Accommodation: ", accommodation)
print("Food: ", food)

print("Remaining balance: ", remaining_balance)
