list_of_nums = list(map(int, input("Enter integers separated by spaces: ").split()))

list_of_nums_sorted = sorted(list_of_nums)

largest_num = list_of_nums_sorted[-1]
smallest_num = list_of_nums_sorted[0]

Difference = largest_num - smallest_num

print("Difference: {}".format(Difference))
