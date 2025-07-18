 # Lyric Tyler
 # June 23rd, 2025
 # P2HW1_TylerLyric
 # A small program that calculates and displays the total 

budget = float(input("Enter your preferred budget: "))
destination = input("What's your desired travel destination?: ")
gas = float(input("Enter the amount of money spent on gas: "))
accommodation = float(input("Enter the amount of money spent on accommodations: "))
food = float(input("Enter the amount of money spent on food: "))

expenses = gas + accommodation + food
remaining_balance = budget - expenses

location = destination
intial_budget = budget

print("--------Travel Expenses--------")
print(f"{'Location:':<15} {destination}")
print(f"{'Initial Budget:':<15} ${budget}")
print(f"{'Fuel:':<15} ${gas}")
print(f"{'Accommodation:':<15} ${accommodation}")
print(f"{'Food:':<15} ${food}")
print("-------------------------------")

print(f"{'Remaining Balance:':<15} ${remaining_balance}")
