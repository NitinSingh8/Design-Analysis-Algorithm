# count sort

from collections import defaultdict


def count_sort(elements):
    # occurrence_of_elements = defaultdict(int)
    max_element = max(elements)

    occurrence_of_elements = [0] * (max_element + 1)

    for i in elements:
        occurrence_of_elements[i] += 1

    # performing cumulative sum on (occurrence_of_elements)list

    for i in range(1, max_element + 1):
        occurrence_of_elements[i] += occurrence_of_elements[i - 1]

    # right shift by 1 index

    for i in range(max_element, 0, -1):
        occurrence_of_elements[i] = occurrence_of_elements[i - 1]
    occurrence_of_elements[0] = 0

    # make the sorted list
    li = [0] * (len(elements))
    for i in elements:
        position = occurrence_of_elements[i]
        li[position] = i
        occurrence_of_elements[i] += 1

    return li


# declare the elements
elements = [5, 4, 2, 3, 1, 4, 2]

# call the functions
elements = count_sort(elements)

# print the elements
print(elements)
