from test_framework import generic_test


def calculate_largest_rectangle(heights):

    def find_pillars(h):
        stk, pillars = [], []
        for i in range(len(h)):
            if not stk:
                pillars.append(-1)
            else:
                while stk and stk[-1][0] >= h[i]:
                    stk.pop()
                if not stk:
                    pillars.append(-1)
                else:
                    pillars.append(stk[-1][1])
            stk.append((h[i], i))
        return pillars

    l = find_pillars(heights)
    r = [len(heights) - i - 1 for i in list(reversed(find_pillars(list(reversed(heights)))))]

    area = 0
    for i in range(len(heights)):
        area = max(area, heights[i] * (r[i]-(l[i]+1)))

    return area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
