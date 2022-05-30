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

restricted_items = ["cigarettes", "wine", "beer", "whiskey"]

shopping_list = reading_list()

waiting_time = 0

if customer_age < 18:
    for i in shopping_list:
        if i not in restricted_items:
            waiting_time = waiting_time + 30


    if waiting_time != 0:
        print(f"Some items are not available for minors. If requested, they have been removed from the list and your waiting time has been adjusted. Please wait {waiting_time} seconds.")
    else: 
        print("Our store can't sell any of those products to minors.")

else: 
    print(f"Your waiting time is {len(shopping_list) * 30} seconds.") 

