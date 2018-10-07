import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class ListNode:
    __slots__ = "data", "next"

    def __init__(self, data, next):
        self.data = data
        self.next = next


def list_pivoting(L, k):
    if not L: return
    tail, n = L, 1
    while tail.next:
        tail, n = tail.next, n + 1

    def move_to_end(prev, node, tail):
        new_node = None
        if node.next:
            prev.next = new_node = node.next
            tail.next, node.next = node, None
            tail = node
        if new_node:
            return new_node, tail
        else:
            return node, tail

    prev, head, m = ListNode(0, L), L, n
    while m:
        if head.data == k:
            if head is L:
                L = head.next if head.next else L
            head, tail = move_to_end(prev, head, tail)
        else:
            head, prev = head.next, prev.next
        m -= 1

    prev, head = ListNode(0, L), L
    while n:
        if head.data > k:
            if head is L:
                L = head.next if head.next else L
            head, tail = move_to_end(prev, head, tail)
        else:
            head, prev = head.next, prev.next
        n -= 1

    return L


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
