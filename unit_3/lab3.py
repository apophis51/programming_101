import random

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
    score = score % 10
    if score >= 5:
        return "+"
    else:
        return "-"
        #test
def compare(score, rival):
    if score > rival:
        print("You did better then your rival")
    if score < rival:
        print("Your rival did better")
    if score == rival:
        print("You both did the same.")



print("\n\nenter a score (0-100): ", end=""); score = int(input())
user_1 = grade(score)
print(f"You got a {score} which is a {user_1}{magnitude(score)}. ",end="")
rival = random.randint(0,100)
user_2 = grade(rival)
print(f" And your rival got a {rival} which is a {user_2}{magnitude(rival)}")
compare(score,rival)
