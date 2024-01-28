def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
    if (swapped == False):
        return input_list

unsorted_list = [60, 10, 20, 15, 30, 70, 55, 65, 35, 40, 45, 25, 50]
sorted_list = bubble_sort(unsorted_list.copy())

# n = len(sorted_list)
# result = False
# first = sorted_list[0]
# last = sorted_list[n-1]

def binary_search(element, input_list):
    first, last = 0, len(input_list)-1
    while first <= last:
        mid = (first + last) // 2
        if element == input_list[mid]:
            return mid
        elif element > input_list[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return -1


element_to_find = 35
result_index = binary_search(element_to_find, sorted_list)

print(f"Неотсортированный список: {unsorted_list}")
print(f"Отсортированный список: {sorted_list}")
if result_index != -1:
    print(f"Элемент {element_to_find} найден на позиции {result_index}.")
else:
    print(f"Элемент {element_to_find} не найден в списке.")

