#!/usr/bin/env python3

def play_with_arrays(arr):
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)

    unique_list = list(unique_elements)

    return unique_list

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [i+2 for i in original_array]
c = [i for i in new_array if i > 5]
result = play_with_arrays(c)
print(original_array)
print(result)