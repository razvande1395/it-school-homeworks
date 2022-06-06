import random

def create_list():

    product_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    product_names = ["bread", "wine", "bacon", "apples", "appricots", "pineapple", "eggs", "sugar", "oil", "salt"]
    package_color = ["yellow", "white", "black", "blue", "red", "green", "teal", "magenta", "purple", "cyan"]
    price = [20, 40, 60, 80, 100, 120]

    item_list = []

    for i in range(10):
        
        x = random.choice(product_id)
        product_id.remove(x)
        y = random.choice(product_names)
        product_names.remove(y)
       
        product = { "id" : x, "name" : y, "package_color" : random.choice(package_color), "price" : random.choice(price) }
        
        item_list.append(product)

    return item_list

item_list = create_list()

for i in range(len(item_list)):
    print(item_list[i])

print(" ")   

item_list.remove(random.choice(item_list))

for i in range(len(item_list)):
    print(item_list[i]["name"], end = " ")
    print(item_list[i]["price"])

print(" ")

x = random.choice(range(len(item_list)))

item_list[x]["id"] = 12
item_list[x]["name"] = "chips"
item_list[x]["package_color"] = "orange"
item_list[x]["price"] = random.choice(range(250))

for i in range(len(item_list)):
    print(item_list[i])