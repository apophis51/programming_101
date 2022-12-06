#Never ending game loop
while 4 > 1 :

    
#First User Input Question
    print("\n\n\nGive me a gender that is female or male:  ", end=""); Word_1 = input() 

#Next Is my logic that pairs a female with a male and vice versa
    if Word_1 == "female":
        Word_2 = "male"
    else:
        Word_2 = "female"

#More Questions for User
    print("Give me a color:  ", end=""); Word_3 = input()
    print("Give me a type of animal:  ", end=""); Word_4 = input()
    print("Give me another color:  ", end=""); Word_5 = input()
    print("Give me another animal:  ", end=""); Word_6 = input()
    print("Give me the name of a hobby: ", end=""); Word_7 = input()
    print("Give me a day of the week:  ", end=""); Word_8 = input()
    print("Give me a 9 digit number: ", end=""); Word_9 = input()


#Next is the output
    print(f"\n\n\n\nATTENTION: {Word_1.upper()} {Word_4.upper()} SEEKING A {Word_2.upper()} {Word_6.upper()} !!!!!!")
    print(f"\n\nI am a {Word_1} {Word_3} {Word_4}. Seeking a {Word_2} {Word_5} {Word_6}. ")
    print(f"I like to go {Word_7}. We should go out on {Word_8}.")
    print(f"Call me at {Word_9}.") 
    print("Chow ;) <3\n\n\n\n")

#Extra Challenge 1
    print("Give me a number:  ", end=""); Number_1 = input()
    print("Give me another Number:  ", end=""); Number_2 = input()

    print(f"{Number_1} + {Number_2} = ", int(Number_1) + int(Number_2))

