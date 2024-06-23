list = [-4,-3,-2,-99,56,-56,2,12,-5]
def max_number_in_list(list):
    max = list[0]

    for i in list:
        if i > max:

            max = i
    return max

print(max_number_in_list(list))