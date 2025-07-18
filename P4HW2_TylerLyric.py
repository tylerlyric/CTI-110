# Ask the user to enter an employee name
employee_name = input("Enter employee's name or 'Done' to stop: ")

# Initialize totals before the loop
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Establish overtime bonus
overtime_bonus = 1.5

while employee_name != "Done":
    # Enter the employee's pay rate and number of hours
    pay_rate = float(input("What is the employee's pay rate?: "))
    hours_worked = float(input("How many hours did they work this pay period?: "))

    # Define the terms of regular hours and overtime
    if hours_worked > 40:
        overtime = hours_worked - 40
        regular_hours = 40
    else:
        overtime = 0
        regular_hours = hours_worked

    # Calculate base pay, overtime pay, and gross pay
    base_pay = regular_hours * pay_rate
    overtime_pay = overtime * pay_rate * overtime_bonus
    gross_pay = base_pay + overtime_pay

    # Update the totals for pay and employees
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += base_pay
    total_gross_pay += gross_pay

    # Display employee summary
    print("------ Payroll Summary ------")
    print(f"Employee Name:    {employee_name}")
    print(f"Regular Pay:      ${base_pay:.2f}")
    print(f"Overtime Pay:     ${overtime_pay:.2f}")
    print(f"Gross Pay:        ${gross_pay:.2f}")
    print("-------------------------------")

    # Run again for next employee (if any)
    employee_name = input("Enter employee's name or 'Done' to stop: ")

# Show all totals
print("======= Final Payroll Report =======")
print(f"Total Employees Entered: {total_employees}")
print(f"Total Overtime Pay:      ${total_overtime_pay:.2f}")
print(f"Total Regular Pay:       ${total_regular_pay:.2f}")
print(f"Total Gross Pay:         ${total_gross_pay:.2f}")
print("====================================")

