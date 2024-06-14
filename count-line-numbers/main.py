your_files = input("Enter the your file name: ")
def count_line_numbers(filename):
    with open(filename) as f:
        line_number = f.readlines()
        return len(line_number)

print(count_line_numbers(your_files))

