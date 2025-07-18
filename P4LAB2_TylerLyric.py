# Lyric Tyler
# July 8th, 2025
# P4LAB3
# Create a program that produces a multiplication table

# Allows for response to the rerun prompt
rerun = "Yes"

# Make it so that a value can be entered
while rerun == "Yes":
    user_input = int(input("Enter an integer: "))

# Make it so that the value is in the range of 1 to 12 only
    if 0 <= user_input <= 12:
        print(f"Multiplication table for {user_input}: ")
        for i in range(1, 13):
            print(f"{user_input} x {i} = {user_input * i}")
        
    else:
        print("The integer entered is not within the limited range.")

# Ask the user if they want to rerun the program
rerun = input("Do you wish to run the program again? (Yes/No): ")
