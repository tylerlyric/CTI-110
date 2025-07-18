# Lyric Tyler
# June 30th, 2025
# P3HW1
# This program takes a number grade, determines average, and displays the letter grade for average.

# Enter grades for six modules
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
              
# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

# Determine letter grade for average
if average >= 90:
    print("Your grade is: A")
    
else:
    if average >= 80:
        print("Your grade is: B")
        
    else:
        if average >= 70:
            print("Your grade is: C")
            
        else:
            if average >= 60:
                print("Your grade is: D")
                
            else:
                print("Your grade is: F")

# Finish this
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average Grade: {average:.2f}")




