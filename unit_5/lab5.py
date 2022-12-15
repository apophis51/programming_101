import random
import string


all_characters =  string.ascii_letters + string.digits + string.punctuation





user_password = ""
password_length = int(input("\n\nHow big of a password do you want? "))

while password_length != 0:
    #user_password = user_password + random.choice(password_picker)
    user_password = user_password + random.choice(all_characters)
    password_length -= 1


print("\nHere is your brand spanking new password: ", user_password)