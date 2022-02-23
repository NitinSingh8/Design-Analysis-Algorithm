# Merge Sort Algorithm (Divide and Conquer Algorithm)


def merge_sort(elements):
    length = len(elements)  # length of elements
    if length > 1:
        mid = length >> 1  # find the middle index of elements list/array
        left_side = elements[:mid]
        right_side = elements[mid:]

        merge_sort(left_side)  # Left side sort recursively
        merge_sort(right_side)  # right side sort recursively

        # when recursion will reach at base condition then it started merging
        # below code for merging tow sorted list/array (left_side, right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                elements[k] = left_side[i]
                i += 1
            else:
                elements[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            elements[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            elements[k] = right_side[j]
            j += 1
            k += 1


# elements = [5, 1, 3, 9, 7, 2]
elements = [5, 4, 3, 2, 1, 9]

merge_sort(elements)  # Calling the function

print(elements)  # At the end print the sorted list/array
