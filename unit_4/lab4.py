import random


#Function to calculate the Winner
def calculate_winner(computer_selection,user_selection):

        if computer_selection == user_selection:
            return "a TIE!"
        elif user_selection == "Rock" and computer_selection == "Paper":
            return "computer"
        elif user_selection == "Rock" and computer_selection == "Scissors":
            return "human"
        elif user_selection == "Paper" and computer_selection == "Rock":
            return "human"
        elif user_selection == "Paper" and computer_selection == "Scissors":
            return "computer"
        elif user_selection == "Scissors" and computer_selection == "Rock":
            return "computer"
        elif user_selection == "Scissors" and computer_selection == "Paper":
            return "human"      

choices = ["Rock","Paper","Scissors"]

print("Welcome to Rock, Paper, Scissors! \
    \
    \n\nYour options are:\n")
    
for x in choices:
    print(f"-{x}")

user_selection = input( "\nEnter your selection:" )



#computer_selection = random.randint(1,3)
computer_selection = random.choice(choices)


#print the output   
print(f"\n\nThe computer picked {computer_selection} and you picked {user_selection}. The winner is: {calculate_winner(computer_selection,user_selection)}")
     

    

