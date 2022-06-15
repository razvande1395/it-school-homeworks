import time

start_time = time.time()

mobile_keys = {
    "0" : [" "],
    "1" : [".", ",", "?", "!", ":"],
    "2" : ["a", "b", "c"],
    "3" : ["d", "e", "f"], 
    "4" : ["g", "h", "i"],
    "5" : ["j", "k", "l"],
    "6" : ["m", "n", "o"],
    "7" : ["p", "q", "r", "s"],
    "8" : ["t", "u", "v"],
    "9" : ["w", "x", "y", "z"]
}

user_message = input("Please insert the message you want to decode: ")

for i in user_message:
    for j in mobile_keys.keys():
        if i.lower() in mobile_keys[j]:
            for k in range(mobile_keys[j].index(i.lower()) + 1):
                print(j, end = "")
            break


end_time = time.time()
print()
print(f"The execution time is {end_time - start_time}")
