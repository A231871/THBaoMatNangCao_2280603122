def delete_item(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = delete_item(my_dict, key_to_delete)

if result:
    print(f"Key '{key_to_delete}' deleted successfully.")
else:
    print(f"Key '{key_to_delete}' not found in the dictionary.")
print("Updated dictionary:", my_dict)
