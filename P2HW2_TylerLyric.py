#Lyric Tyler
#June 24th, 2025
#P2HW2_TylerLyric
# Calculate grades and find the lowest, highest, sum of, and average grades.



module1_grade = float(input("Enter grade for Module 1: "))
module2_grade = float(input("Enter grade for Module 2: "))
module3_grade = float(input("Enter grade for Module 3: "))
module4_grade = float(input("Enter grade for Module 4: "))
module5_grade = float(input("Enter grade for Module 5: "))
module6_grade = float(input("Enter grade for Module 6: "))

course_grades = [module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade]

lowest_grade = min(course_grades)
highest_grade = max(course_grades)

all_grades = sum(course_grades)
quantity_grades = len(course_grades)

grade_average = all_grades / quantity_grades

print("------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade}")
print(f"{'Highest Grade:':<20} {highest_grade}")
print(f"{'Grade Sum:':<20} {all_grades}")
print(f"{'Average:':<20} {grade_average:.2f}")
print("-------------------------------")


