# Depth First Search Algorithm

# For Depth First Search : Use Recursion / Stack


from collections import defaultdict


def dfs(adjacent_list, start, path, isVisited):
    path.append(start)
    isVisited[start] = True
    for edge in adjacent_list[start]:
        if isVisited[edge] == False:
            path = dfs(adjacent_list, edge, path, isVisited)
    return path

    # Make the adjacent list first by taking input


# v, e = map(int, input().split())
#
# adjacent_list = defaultdict(list)
#
# for i in range(e):
#     a, b = map(str, input().split())
#     adjacent_list[a].append(b)
#     adjacent_list[b].append(a)
#
# print(adjacent_list)

# Or Take default adjacent list

adjacent_list = {'A': ['B', 'D'], 'B': ['A', 'C', 'D'], 'C': ['B', 'D'], 'D': ['C', 'A', 'B']}

# Let Assume our vertices name are in alphabetic like A, B, C etc
# So we will start from A
start = 'A'
path = []  # this will have our dfs path
isVisited = defaultdict(bool)

# now lets call the function
path = dfs(adjacent_list, start, path, isVisited)

# print path
print("path is : ", *path)
