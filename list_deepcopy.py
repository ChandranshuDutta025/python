import copy

original_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[0][0] = 99

print(original_list)      # Output: [[1, 2], [3, 4]]
print(deep_copied_list)   # Output: [[99, 2], [3, 4]]
