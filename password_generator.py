import random, string
pass_len = (input("How long would You like Your password :) ? : "))
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for number in range (int(pass_len)):
    password += random.choice(all_characters) 
print("Your password is:", password)

