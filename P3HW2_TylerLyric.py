# Lyric Tyler
# June 30th, 2025
# P3HW2
# Program describing

# Ask user for employee information
name = input("Enter the employee's full name: ")
hours = float(input("Enter the number of hours worked: "))
pay = float(input("Enter the employee's pay rate: "))

# Hours and applying overtime difference
normal_hours = 40
overtime_bonus = 1.5

# Determine the pay for normal hours and overtime
if hours > normal_hours:
    overtime = hours - normal_hours
    regular_hours = normal_hours
else:
    overtime = 0
    regular_hours = hours

# Calculate the differences in pay by hours and overtime bonus
base_pay = regular_hours * pay
overtime_pay = overtime * pay * overtime_bonus
gross_pay = base_pay + overtime_pay

# Print results
print("---------------------------------------------")
print(f"Employee name:    {name}")
print()
print(f"{'Hours Worked':<14}{'Pay Rate':<11}{'Overtime':<10}{'Overtime Pay':<15}{'Base Pay':<15}{'Gross Pay':<10}")
print("--------------------------------------------------------------------------")
print(f"{hours:<14.1f}{pay:<11.1f}{overtime_bonus:<10.1f}{overtime_pay:<15.2f}${base_pay:<14.2f}${gross_pay:.2f}")
