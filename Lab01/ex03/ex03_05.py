def count_times_appears(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Enter a list of words separated by space: ")
words_list = input_string.split()

words_count = count_times_appears(words_list)
print("Word count:", words_count)
