import random

#Method to grade the score and return the letter grade
def grade(score):
    letter_grade = ""
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    elif score <= 59:
        letter_grade = "F"
    return letter_grade

#Grade '+' or '-' Extra challenge 2 
def magnitude(score):
   
    if score <= 59:
        return ""
    score = score % 10

    if score >= 7:
        return "+"
    else:
        return "-"

#method to compare user score to rival score      
def compare(user, rival):
    if user > rival:
        print("You did better then your rival")
    if user < rival:
        print("Your rival did better")
    if user == rival:
        print("You both did the same.")


#Start of Program: Get the score from user 1
user_score = int(input("\n\nenter a score (0-100): "))

#Call the Grading method to calculate the letter grade of the user
user_grade = grade(user_score)

#Print the User score, grade, and grade magnitude "+" or "-" 
print(f"You got a {user_score} which is a {user_grade}{magnitude(user_score)}. ",end="")


#Get the Rival Score from Random, and then call the grading method to get the letter grade
rival_score = random.randint(0,100)
rival_grade = grade(rival_score)

#Print the Rival score, grade, and grade magnitude "+" or "-" 

print(f" And your rival got a {rival_score} which is a {rival_grade}{magnitude(rival_score)}")

#Call the method that compares user_score to rival_score
compare(user_score,rival_score)
