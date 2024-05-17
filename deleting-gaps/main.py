text =(input("Enter the Text: "))
def deleting_gaps(text):
    text = text.replace(" ", "")
    return text

print(deleting_gaps(text))