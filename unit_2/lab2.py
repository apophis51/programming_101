#Never ending game loop
while 4 > 1 :

    
#First User Input Question
    gender_1 = input("\n\n\nGive me a gender that is female or male:  ",) 

#Next Is my logic that pairs a female with a male and vice versa
    if gender_1 == "female":
        gender_2 = "male"
    else:
        gender_2 = "female"

#More Questions for User
    color_1 = input("Give me a color:  ") 
    animal_1 = input("Give me a type of animal:  ") 
    color_2 = input("Give me another color:  ") 
    animal_2 = input("Give me another animal:  ") 
    hobby = input("Give me the name of a hobby: ")
    day_of_the_week = input("Give me a day of the week:  ") 
    nine_digit_number = input("Give me a 9 digit number: ") 


#Next is the output
    print(f"\n\n\n\nATTENTION: {gender_1.upper()} {animal_1.upper()} SEEKING A {gender_2.upper()} {animal_2.upper()} !!!!!!")
    print(f"\n\nI am a {gender_1} {color_1} {animal_1}. Seeking a {gender_2} {color_2} {animal_2}. ")
    print(f"I like to go {hobby}. We should go out on {day_of_the_week}.")
    print(f"Call me at {nine_digit_number}.") 
    print("Chow ;) <3\n\n\n\n")

#Extra Challenge 1
    number_1 = input("Give me a number:  ")
    number_2 = input("Give me another Number:  ")

    print(f"{number_1} + {number_2} = ", int(number_1) + int(number_2))

