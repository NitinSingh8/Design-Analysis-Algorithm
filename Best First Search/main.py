# Best First Search

# For best first search use queue or dequeu

from collections import defaultdict, deque


def bfs(adjacent_list, start, path, isVisited):
    queue = deque()
    queue.append(start)
    isVisited[start] = True
    path.append(start)
    while len(queue) != 0:
        element = queue.popleft()
        # path.append(element)
        for i in adjacent_list[element]:
            if not isVisited[i]:
                queue.append(i)
                path.append(i)
                isVisited[i] = True
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
path = bfs(adjacent_list, start, path, isVisited)


# print path
print("path is : ", *path)
