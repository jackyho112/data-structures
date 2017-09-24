# python3

import sys

class Rope:
    def __init__(self, s):
        self.s = s
    def result(self):
        return self.s
    def process(self, i, j, k):
        string = self.s[i:j+1]
        self.s = self.s[:i] + self.s[j+1:]
        if k == 0:
            self.s = string + self.s
        else:
            self.s = self.s[:k] + string + self.s[k:]

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
