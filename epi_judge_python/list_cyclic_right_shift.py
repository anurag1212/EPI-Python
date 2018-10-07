from test_framework import generic_test


class ListNode:
    __slots__ = "data", "next"

    def __init__(self, val, next):
        self.next = next
        self.data = val


def cyclically_right_shift_list(head, k):
    if not head: return
    dummy_head = ListNode(0, head)
    n, new_head, prev = 1, head, dummy_head
    while new_head.next:
        new_head, n = new_head.next, n+1
    last, new_head, to_shift = new_head, head, n - (k % n)
    while to_shift:
        new_head, to_shift, prev = new_head.next, to_shift - 1, prev.next
    prev.next = None
    if new_head:
        last.next = head
        return new_head
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
