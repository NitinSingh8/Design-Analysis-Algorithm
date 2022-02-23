# Quick Sort Algorithm (Divide and Conquer Algorithm)


def get_partition(elements, low, high):  # Function to put last element at right position and return that right position
    pivot = elements[high]

    i = low - 1
    for j in range(low, high):
        if elements[j] < pivot:
            i += 1
            elements[j], elements[i] = elements[i], elements[j]

    elements[i + 1], elements[high] = elements[high], elements[i + 1]
    return i + 1


def quick_sort(elements, low, high):  # Recursive calling the function on sub part elements
    if low < high:
        partition = get_partition(elements, low, high)
        quick_sort(elements, low, partition - 1)
        quick_sort(elements, partition, high)


elements = [5, 1, 3, 9, 7, 2]

# Calling the main Function
quick_sort(elements, 0, len(elements) - 1)

print(elements)  # At the end printing the sorted list/elements
