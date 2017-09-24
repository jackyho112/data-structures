# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder_recursive(self, index):
    if self.left[index] != -1:
      self.inOrder_recursive(self.left[index])

    self.result.append(self.key[index])

    if self.right[index] != -1:
      self.inOrder_recursive(self.right[index])

  def inOrder(self):
    self.result = []

    self.inOrder_recursive(0)
    return self.result

  def preOrder_recursive(self, index):
    self.result.append(self.key[index])
    if self.left[index] != -1:
      self.preOrder_recursive(self.left[index])
    if self.right[index] != -1:
      self.preOrder_recursive(self.right[index])

  def preOrder(self):
    self.result = []

    self.preOrder_recursive(0)
    return self.result

  def postOrder_recursive(self, index):
    if self.left[index] != -1:
      self.postOrder_recursive(self.left[index])
    if self.right[index] != -1:
      self.postOrder_recursive(self.right[index])
    self.result.append(self.key[index])

  def postOrder(self):
    self.result = []

    self.postOrder_recursive(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
