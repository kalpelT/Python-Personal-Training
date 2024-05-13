capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

text = input("Enter the text: ")
def check_capital_letter(text):
    constant = 0
    for i in text:
        if i in capital_letter:
            constant += 1
    return constant

print("Number of The Capital Letter in the text:",check_capital_letter(text))