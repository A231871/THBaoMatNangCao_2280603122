def divisable_by_5(binary):
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        return True
    else:
        return False

inputtedbinarylist = input("Enter a list of binary numbers separated by commas: ")
binarylist = inputtedbinarylist.split(",")
numbers_divisible_by_5 = [num for num in binarylist if divisable_by_5(num)]

if len(numbers_divisible_by_5) == 0:
    print("No numbers in the list are divisible by 5.")
else:
    print("The numbers in the list that are divisible by 5 are: " + ", ".join(numbers_divisible_by_5))
# The code above takes a list of binary numbers as input, checks which of them are divisible by 5 when converted to decimal, and prints those numbers.