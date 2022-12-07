print("enter the first word: ", end=""); firstword = input()
print("enter the second word: ", end=""); secondword = input()

anagram = True
if len(firstword) == len(secondword):
    for x in secondword:
        if x not in firstword:
            anagram = False
            print(f"{firstword} and {secondword} are not anagrams")

if anagram == True:
    print(f"{firstword} and {secondword} are anagrams")

    


