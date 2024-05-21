list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [2, 3, 5, 7, 10, 11, 14, 15, 18]


set1 = set(list1)
set2 = set(list2)

common_element = set1 & set2
common_element_list = list(common_element)

print(common_element_list)

