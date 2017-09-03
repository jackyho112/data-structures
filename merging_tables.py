# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [0] * n
parents = list(range(0, n))
answers = [max(lines)]

def getParent(table):
    balance_parents = []

    index = table
    while index != parents[index]:
        balance_parents.append(parents[index])
        index = parents[index]

    for i in balance_parents:
        parents[i] = index

    # find parent and compress path
    return index

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    if rank[realSource] >= rank[realDestination]:
        parents[realSource] = realDestination
    else:
        parents[realDestination] = realSource
        if rank[realSource] == rank[realDestination]:
            rank[realSource] += 1

    lines[realDestination] += lines[realSource]
    lines[realSource] = 0

    if answers[-1] < lines[realDestination]:
        answers.append(lines[realDestination])

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(answers[-1])
