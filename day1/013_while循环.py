__author__ = 'fke'

age_of_fke = 57
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_fke:
        print("yes, you got it.")
    elif guess_age > age_of_fke:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
    if count == 3:
        countine_confirm = input("do you want to keep guessing..?(Enter any key continue)")
        if countine_confirm != 'n':
            count = 0



