import random



def winner(computer_selection,selection):

        if computer_selection == selection:
            return "its a TIE!"
        if selection == "Rock" and computer_selection == "Paper":
            return "computer"
        if selection == "Rock" and computer_selection == "Scissors":
            return "human"
        if selection == "Paper" and computer_selection == "Rock":
            return "human"
        if selection == "Paper" and computer_selection == "Scissors":
            return "computer"
        if selection == "Scissors" and computer_selection == "Rock":
            return "computer"
        if selection == "Scissors" and computer_selection == "Paper":
            return "human"

#1 hot encoding    Rock = 3 , Paper = 2 , Scissors = 1
def computer_choice(computer_selection):
    if computer_selection == 3:
        return "Rock"
    elif computer_selection == 2:
         return "Paper"
    elif computer_selection == 1:
         return "Scissors"       

games = "four"
for x in games:

    print("Welcome to Rock, Paper, Scissors! \
    \
    \n\nYour options are:\
    \
    \n\n- Rock\
    \n- Paper\
    \n- Scissors\
    \
    \n\nEnter your selection:", end="") ; selection = input()

    computer_selection = random.randint(1,3)

   

    print(f"\n\nThe computer picked {computer_choice(computer_selection)} and you picked {selection}. The winner is: {winner(computer_choice(computer_selection),selection)}")
     

    

