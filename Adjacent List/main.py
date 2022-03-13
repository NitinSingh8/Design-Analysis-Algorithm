# Make the adjacent list of Graph

from collections import defaultdict

v,e = map(int,input("Enter the number of vertices and edges : ").split())

adjacent_list = defaultdict(list)


# Taking the input/edges

for i in range(e):
    a,b = map(int,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)


# Print the adjacent list
for key in adjacent_list:
    print(key,adjacent_list[key])



