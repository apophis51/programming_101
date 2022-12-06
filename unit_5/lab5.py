import random

password_picker = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p" \
,"q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","\""]

user_password = ""
print("\n\nHow big of a password do you want? ", end=''); numbers = int(input())


while numbers != 0:
    user_password = user_password + random.choice(password_picker)
    numbers -= 1


print("\nHere is your brand spanking new password :", user_password)