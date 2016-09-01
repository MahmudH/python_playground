import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number(chances):
    user_input = int(input("Enter a number between 0 and 9, you have {} chances: ".format(chances)))
    if user_input in magic_numbers:
        return "You got the number right"
    else:
        return "You got the number wrong"

def run_program_x_times(chances):
    for attempt in range(chances):
        print "This is attempt {}".format(attempt)
        print ask_user_and_check_number(chances)
    print "The random numbers were: {}".format(magic_numbers)

run_program_x_times(5)

