original_list = [[1, 2], [3, 4]]
copied_list = original_list.copy()

copied_list[0][0] = 99

print(original_list)  # Output: [[99, 2], [3, 4]]
print(copied_list)    # Output: [[99, 2], [3, 4]]
