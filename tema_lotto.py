import random

def generate_numbers():
    lottery_numbers = []

    for i in range(1, 50):
        lottery_numbers.append(i)

    winning_numbers = random.sample(lottery_numbers, 6)
    return winning_numbers


winning_numbers = generate_numbers()

print(f"The winning numbers are: {winning_numbers} ")


