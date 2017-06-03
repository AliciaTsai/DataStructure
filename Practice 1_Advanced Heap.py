class MaxHeap():
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    child = right
            if self._data[child] > self._data[j]:
                self._swap(j, child)
                self._downheap(child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def get_data(self):
        return self._data

    def is_empty(self):
        return self._data == []

    def push(self, value):
        self._data.append(value)
        self._upheap(len(self._data) - 1)

    def top(self):
        if self.is_empty():
            return 0
        else:
            return self._data[0]

    def pop(self):
        if self.is_empty():
            return 0
        else:
            self._swap(0, len(self._data) - 1)
            last_one = self._data.pop()
            self._downheap(0)
            return last_one


# file = open('HW1_2.txt', 'r')
# test_case = int(file.readline())

size = int(input())
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
heap = MaxHeap()
result = 0
s_sum = []

for i in range(size):
    for j in range(size):
        s_sum.append(s1[i] + s2[j])

for i in range(size):
    heap.push(s_sum[i])

for j in range(size, len(s_sum)):
    if s_sum[j] < heap.top():
        heap.pop()
        heap.push(s_sum[j])

for k in heap.get_data():
    result += k

print(result)