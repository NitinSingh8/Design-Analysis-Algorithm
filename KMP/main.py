# KMP algorithm


# declaring the function to get prefix list
def get_prefix(pattern):


    length = len(pattern)  # length of pattern

    prefix_list = [0] * length  # making default prefix array containing element 0 in all position

    for i in range(1, length):
        j = prefix_list[i - 1]

        if pattern[j] == pattern[i]:
            prefix_list[i] = j + 1
        else:
            k = i - j + 1
            if k > i:
                prefix_list[i] = 0
            else:
                temp = 0
                start, end = 0, k
                for _ in range(j):
                    if pattern[start] == pattern[end]:
                        temp += 1
                        start += 1
                        end += 1
                    else:
                        start = 0

                        temp = 0
                prefix_list[i] = temp
    return prefix_list


# declare the main function
def kmp(text, pattern):
    # calculating prefix array/list
    prefix_list = get_prefix(pattern)

    lp = len(pattern)  # length of pattern (lp)
    lt = len(text)  # length of text (lt)
    i = 0
    j = 0
    pos = []  # list for storing all the position of pattern present in text

    while i < lt:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix_list[j - 1]
            else:
                i += 1
        if j == lp:
            pos.append(i - lp)
            j = 0

    return pos  # returning list


# input
text = "mississippi"  # text
pattern = "issip"  # pattern

pos_of_index = kmp(text, pattern)
print(pos_of_index)
