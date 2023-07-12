import random 

again = True

while again:
    print(random.randint(1, 6))
    another_roll = input("type here to roll dice (y/n) ")
    if another_roll.lower() == "y":
        continue
    else:
        break