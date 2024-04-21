your_files = input("Enter the your file name: ")
count = 0
which_line = int(input("Enter the line: "))

with open(your_files, encoding= "utf-8") as f:

    for x in f:
        count += 1
        if count == which_line:
            print(x, end=" ")
            break