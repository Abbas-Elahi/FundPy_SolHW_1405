import random

number = random.randint(1, 100)
count = 0

while count < 7:
    x = int(input("Guess a number: "))
    count += 1

    if x == number:
        print("You win!")
        print("Number of guesses:", count)
        break

    elif x < number:
        print("Try a bigger number")

    else:
        print("Try a smaller number")

    print("Remaining:", 7 - count)

else:
    print("You lost!")
    print("The number was:", number)
