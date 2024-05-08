"""
The basic algorithm of insertion sort is:
For each element:
 - put all smaller elements to the left
 - put all larger elements to the right
"""


def insertion_sort(list_to_sort):
    for index in range(1,len(list_to_sort)):

        current_value = list_to_sort[index]
        position = index

        while position > 0 and list_to_sort[position-1] > current_value:
            list_to_sort[position] = list_to_sort[position-1]
            position -= 1

    list_to_sort[position] = current_value

l = [54,26,93,17,77,31,44,55,20]
insertion_sort(l)
print(l)
