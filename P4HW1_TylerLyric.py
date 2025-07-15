#Lyric Tyler
#July 10th, 2025
#P4HW1_TylerLyric
# Calculate grades and display them with a letter grade.

# Ask how many scores the user wants to enter
amount_scores = int(input("How many scores would you like to enter? "))

# Create a list to store the entered values
score_list = []

# Collect the scores from the user
for i in range(amount_scores):
    score = float(input(f"Enter score {i+1}: "))

    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input(f"Re-enter score {i+1}: "))

    score_list.append(score)

# Find the lowest score
lowest_score = min(score_list)

# Remove the lowest score from the list
score_list.remove(lowest_score)

# Calculate the average of the scores without the lowest
average_score = sum(score_list)/len(score_list)

# Determine a letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print("--------Results--------")
      
# Display the lowest score
print(f"Lowest score: {lowest_score}")

# Display the modified list
print(f"Modified list: {score_list}")

#Display the average of the modified list
print(f"Average: {average_score:.2f}")

# Display the grade average with a letter grade
print(f"Final letter grade: {average_score:.2f}")

print("-----------------------")







