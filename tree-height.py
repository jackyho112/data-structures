# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self):
        self.root = False
        self.children = []
        self.depth = 0

    def addChild(self, node):
        self.children.append(node)
        return True

    def setRoot(self):
        self.root = True
        return True

    def find_depth(self):
        if self.depth:
            return self.depth

        depth = 0
        children = self.children
        computed_heights = []

        while len(children):
            depth += 1
            new_children = []

            for child in children:
                if child.depth:
                    computed_heights.append(depth + child.depth)
                elif len(child.children):
                    new_children += child.children

            children = new_children

        computed_heights.append(depth)
        self.depth = max(computed_heights)
        return self.depth

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes = []

                for i in range(0, self.n):
                    self.nodes.append(Node())

                for index, parent_index in enumerate(self.parent):
                    if parent_index == -1:
                        self.nodes[index].setRoot()
                    else:
                        self.nodes[parent_index].addChild(self.nodes[index])

        def compute_height(self):
                depths = []

                for node in self.nodes:
                    depths.append(node.find_depth())

                return max(depths) + 1

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
