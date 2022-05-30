import random

def reading_list():
    
    a = []
    
    while True:
        x = input("Please insert the next item you're buying: ")
        if x != "":
            a.append(x)
        else:
            break

    return a

customer_age = int(input("Please insert your age: "))

#restricted_items = ["cigarettes", "wine", "beer", "whiskey"]

shopping_list = reading_list()


print(f"Unfortunately, {random.choice(shopping_list)} is out of stock right now, we apologize for the incovenience.")



print(f"Your waiting time is {(len(shopping_list) - 1) * 30} seconds")

