def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total


number_list = [0]

done = "keepgoing"
while done == "keepgoing":
    print("enter numbers, one at a time, type done when done: ", end=""); user_input = input()
    if user_input == "done":
        done = "done"
    else:
        number_list.append(int(user_input))

print(sum(number_list))