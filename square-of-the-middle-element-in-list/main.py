my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21]
lenght = len(my_list)

if lenght % 2 == 1:
    middle_index = lenght // 2
    middle_elements = my_list[middle_index - 1:middle_index + 2]

elif lenght % 2 == 0:
    middle_index = lenght // 2
    middle_elements = my_list[middle_index - 1:middle_index + 2]

square_of_middle_elements = [x**2 for x in middle_elements]
print("Square of the middle elements:",square_of_middle_elements)
