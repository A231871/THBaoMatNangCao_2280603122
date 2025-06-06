def create_tuple_list(lst):
    return tuple(lst)

input_list = input("Enter a list of numbers separated by commas: ")
numbers = list(map(int, input_list.split(',')))

tuple_list = create_tuple_list(numbers)
print("Original list:", numbers)
print("Tuple list:", tuple_list)