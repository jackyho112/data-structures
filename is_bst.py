# python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def find_children_min(tree, store, index):
    immediate_child_index = store[index][1]

    if immediate_child_index == -1:
        store[index][3] = tree[index]
        return tree[index]

    current_level = store[immediate_child_index]
    mini = tree[immediate_child_index]

    while current_level[0] != -1:
        if current_level[3] == None:
            child_min = find_children_min(tree, store, current_level[0])
            if child_min < mini:
                mini = child_min
        elif current_level[3] < mini:
            mini = current_level[3]
        current_level = store[current_level[0]]

    store[index][3] = mini

    return mini

def find_children_max(tree, store, index):
    immediate_child_index = store[index][0]

    if immediate_child_index == -1:
        store[index][2] = tree[index]
        return tree[index]

    current_level = store[immediate_child_index]
    maxi = tree[immediate_child_index]

    while current_level[1] != -1:
        if current_level[2] == None:
            child_max = find_children_max(tree, store, current_level[1])
            if child_max > maxi:
                maxi = child_max
        elif current_level[2] > maxi:
            maxi = current_level[2]
        current_level = store[current_level[1]]

    store[index][2] = maxi

    return maxi

def isBinarySearchTree(tree, store):
  for index, node in enumerate(tree):
      childInfo = store[index]

      if childInfo[0] != -1:
          if childInfo[2] != None and childInfo[2] > node:
              return False
          elif find_children_max(tree, store, index) > node:
              return False

      if childInfo[1] != -1:
          if childInfo[3] != None and childInfo[3] < node:
              return False
          elif find_children_min(tree, store, index) < node:
              return False

  return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  store = {}
  for i in range(nodes):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    tree.append(arr[0])
    store[i] = arr[1:]
    store[i].append(None)
    store[i].append(None)
  if isBinarySearchTree(tree, store):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
