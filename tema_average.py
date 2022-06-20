
def read_the_numbers():

    numbers_list = []

    while True:
        x = input("Please insert the next number for the problem: ")
        if x == "" or x == " ":
            break
        else:
            numbers_list.append(int(x))
    
    return numbers_list

def compute_average(numbers_list):
    
    sum = 0
    
    for i in range(len(numbers_list)):
        sum = sum + numbers_list[i]
    
    return sum/len(numbers_list)

def sort_the_list(initial_list, avg):
    
    below_avg_list = []
    avg_list = []
    above_avg_list = []

    for i in range(len(initial_list)):
        if initial_list[i] < avg:
            below_avg_list.append(initial_list[i])
        elif initial_list[i] == avg:
            avg_list.append(initial_list[i])
        else:
            above_avg_list.append(initial_list[i])

    return below_avg_list, avg_list, above_avg_list


initial_list = read_the_numbers()
avg_value = compute_average(initial_list)

print(avg_value)

below_average_list, average_list, above_average_list = sort_the_list(initial_list, avg_value)

print(f"{below_average_list} \n{average_list} \n{above_average_list}")





    

