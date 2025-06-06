def reverse_string(s):
    #Return the reverse of the string s.
    return s[::-1]

input_str = input("Enter a string: ")
print("The reverse of the string is: " + reverse_string(input_str))