import random
quick_picks = []
number_of_quick_picks = int(input('Number of quick picks: '))
for i in range(number_of_quick_picks):
    for j in range(6):
        random_number = random.randint(1,46)
        while random_number in quick_picks:
            random_number = random.randint(1, 46)
        quick_picks.append(random_number)
        quick_picks.sort()
    for k in quick_picks:
        print('{:2}'.format(k), end=" ")
    print()
    quick_picks = []

