print("Set Matrix Zero")

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def solution_1(arr: list[list[int]]):
    pass


print(solution_1(arr=matrix))

print()
print("Rotate Image by 90 degree")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Brute Force
def solution_2(arr: list[list[int]]):
    n = len(arr)
    output_matrix = []
    for i in range(0, len(arr)):
        output_matrix.append([0] * n)

    for i in range(0, n):
        for j in range(0, len(arr[i])):
            output_matrix[i][j] = arr[(n - j) - 1][i]

    return output_matrix


print(solution_2(arr=matrix))
