list = [1,2,3,4,5,6,7,8,9,10]

def multply(list):
    prod = 1
    for i in list:
        prod *= i
    return prod

print("Listedeki elemanların çarpımı:", multply(list))

