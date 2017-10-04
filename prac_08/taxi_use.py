from prac_08.taxi import Taxi
from prac_08.silver_taxi import SilverTaxi

taxis = [Taxi("Prius", 100), SilverTaxi("Limo", 100, 2), SilverTaxi("Hummer", 200, 4)]


def main():
    print("Let's Drive")
    user_input = 'a'
    bill = 0.0
    user_taxi_choice = -1
    while user_input != 'q':
        user_input = input('q)uit, c)hoose taxi, d)rive\n>>>').lower()
        if user_input == 'c':
            for i, taxi in enumerate(taxis):
                print('{} - {}'.format(i, taxi))

            user_taxi_choice = taxis[int(input('Choose taxi: '))]

        elif user_input == 'd':
            user_taxi_choice.start_fare()
            distance = int(input('Drive how far ? '))
            user_taxi_choice.drive(distance)
            print('Your {} trip cost you ${}'.format(user_taxi_choice.name, user_taxi_choice.get_fare()))
            bill += user_taxi_choice.get_fare()
        if user_input != 'q':
            print('Bill to date :${:.2f}'.format(bill))

    print('Total trip cost: ${:.2f}'.format(bill))
    print('Taxis are now:')
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, taxi))


main()
