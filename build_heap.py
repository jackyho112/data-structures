# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def left_child_index(self, index):
    left_child_index = 2 * index + 1

    if left_child_index >= len(self._data):
        return False

    return left_child_index

  def right_child_index(self, index):
    right_child_index = 2 * index + 2

    if right_child_index >= len(self._data):
        return False

    return right_child_index

  def sift_down(self, i):
    index = i
    left_child_index = self.left_child_index(i)
    right_child_index = self.right_child_index(i)

    if right_child_index and self._data[right_child_index] < self._data[index]:
      index = right_child_index

    if left_child_index and self._data[left_child_index] < self._data[index]:
      index = left_child_index

    if i != index:
      self._swaps.append((i, index))
      self._data[i], self._data[index] = self._data[index], self._data[i]
      self.sift_down(index)

  def GenerateSwaps(self):
    for i in range(len(self._data) // 2, -1, -1):
        self.sift_down(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
