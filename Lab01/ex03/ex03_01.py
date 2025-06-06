def cal_even_sum(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum

input_list = input("Enter a list of numbers separated by commas: ")
numbers = list(map(int, input_list.split(',')))

sum_of_evens = cal_even_sum(numbers)
print("Sum of even numbers:", sum_of_evens)