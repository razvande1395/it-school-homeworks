import random

def generate_winning_numbers():
    
    lottery_numbers = []

    for i in range(1, 50):
        lottery_numbers.append(i)

    winning_numbers = random.sample(lottery_numbers, 6)
    return winning_numbers


winning_numbers = generate_winning_numbers()

print(f"The winning numbers are: {winning_numbers} ")


