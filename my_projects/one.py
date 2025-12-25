import random

while True:
    choice = input("Roll the dice : (y/n) ").lower()  # fixed

    items = [1, 2, 3, 4, 5, 6]

    if choice == 'y':
        rand_choice = random.choice(items)
        print("You rolled:", rand_choice)
    elif choice == 'n':
        print("Thanks for playing :)")
        break
    else:
        print("Invalid :(")
