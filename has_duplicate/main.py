def has_duplicate(lst):
    seen = []
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False

print(has_duplicate([1, 2, 3, 2]))  # True
print(has_duplicate([2, 1, 3, 4]))