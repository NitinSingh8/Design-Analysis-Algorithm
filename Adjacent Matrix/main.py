# Make the adjacent matrix by getting edges



v, e = map(int, input("Enter the number of vertices and edges : ").split())  # Getting the number of vertices and edges

adjacent_matrix = [[0] * v for _ in range(v)]

# Enter the edges ( like if 1 is connected to 2 then wrote 1 2)

for i in range(e):
    a, b = map(int, input().split())
    adjacent_matrix[a - 1][b - 1] = 1
    adjacent_matrix[b - 1][a - 1] = 1

# Print the adjacent matrix
for i in adjacent_matrix:
    print(*i)

