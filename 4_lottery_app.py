import random

def menu():
    player_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = player_numbers.intersection(lottery_numbers)
    print("You matched {}. You won {}".format(matched_numbers, 100 ** len(matched_numbers)))

def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    number_set = {int(number) for number in number_csv}
    return number_set

def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

menu()
