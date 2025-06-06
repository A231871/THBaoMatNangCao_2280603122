def access_tuple_list(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Enter a tuple of numbers separated by commas: "))
first, last = access_tuple_list(input_tuple)

print("First element:", first)
print("Last element:", last)