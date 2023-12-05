# from memory_profiler import profile

# @profile(precision=6)
def findPartition(arr, n):
    list_sum = sum(arr)
    i, j = 0, 0

    part = [[True for i in range(n + 1)]
            for j in range(list_sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, list_sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, list_sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                            part[i - arr[j - 1]][j - 1])

    print(part)

    return part[list_sum // 2][n]

def partition_dyn(arr):
    if sum(arr) % 2 != 0:
        return False

    return findPartition(arr, len(arr))
