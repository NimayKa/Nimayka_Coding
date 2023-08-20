def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return reverse_list(lst[1:]) + [lst[0]]

input_list = [1, 2, 3, 4, 5]
output_list = reverse_list(input_list)
print("Reversed List:", output_list)
