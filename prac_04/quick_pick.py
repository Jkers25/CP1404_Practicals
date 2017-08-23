import random

MIN_NUMBER = 1

MAX_NUMBER = 46

number_of_quick_picks = int(input('Number of quick picks: '))
for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(6):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while random_number in quick_picks:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(random_number)
    quick_picks.sort()
    for quick_pick in quick_picks:
        print('{:2}'.format(quick_pick), end=" ")
    print()

