import random
import time

cars = [0, 0, 0]

while max(cars) < 50:

    for i in range(3):
        cars[i] += random.randint(1, 5)

        print(f"Car {i+1}: {'-' * cars[i]}🏎️ {cars[i]}")

    print("--------------------")
    time.sleep(0.5)

winners = []

for i in range(3):
    if cars[i] >= 50:
        winners.append(i + 1)

if len(winners) == 1:
    print("Winner: Car", winners[0])
else:
    print("Tie! Cars:", winners)
