import random

seceret_no = random.randint(1,100)
attempt = 0

print("i have selected ")
print("try to guess it")

while True:
    user_no = int(input("enter your guess no : "))
    attempt += 1
    
    if user_no < seceret_no:
        print("your guess is too low")
    elif user_no > seceret_no:
        print("your guess is too high")
    else:
        print(f"congratulation you guessed it in {attempt} attempts")
        break