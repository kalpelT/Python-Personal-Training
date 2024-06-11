

#sort

student_list = ['Drake', 'John', 'Mark', 'Alex']

alphabetical_list = sorted(student_list)
print(alphabetical_list)

ages = [12,45,31,24,17,19,52]
ages.sort()
print("Ages incrase:",ages)

ages.sort(reverse=True)
print("Ages Decrease:",ages)

numbers = [89,86,45,46,90,98,2,15]
sorted_numbers = sorted(numbers)

print("Original list:",numbers)
print("Sorted List: ",sorted_numbers)

students = [

    {"name": "John", "grade": 90, "height": 185},
    {"name": "Jane", "grade": 60, "height": 167},
    {"name": "Alice", "grade": 80, "height": 155}

]

#sorted by height
sorted_students = sorted(students, key=lambda student: student['height'], reverse=True)
print("Students sorted by height:", sorted_students)

#insertion


def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


numbers = [5, 2, 9]
insertion_sort_descending(numbers)
print("Decrase numbers list:", numbers)