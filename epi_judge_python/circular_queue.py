from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * self._capacity
        self._start, self._end, self._n = 0, 0, 0
        return

    def resize(self, new_capacity):
        item = 0
        new_data = [None] * new_capacity
        walker = self._start
        while walker != self._end:
            new_data[item] = self._data[walker % self._capacity]
            item += 1
            walker = (walker + 1) % self._capacity
        self._data = new_data
        self._capacity = new_capacity
        self._start = 0
        self._end = item

    def enqueue(self, x):
        if self._n < self._capacity - 1:
            self._data[self._end] = x
            self._end = (self._end + 1) % self._capacity
            self._n += 1
        else:
            self.resize(self._capacity * 2)
            self.enqueue(x)
        return

    def dequeue(self):
        if self._n and self._n > self._capacity // 4:
            element = self._data[self._start]
            self._start = (self._start + 1) % self._capacity
            self._n -= 1
        else:
            self.resize(self._capacity // 2)
            return self.dequeue()
        return element

    def size(self):
        return self._n


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
