from test_framework import generic_test


def get_max_trapped_water(heights):
    s, e, maxwater = 0, len(heights) - 1, float('-inf')
    while s < e:
        maxwater = max(maxwater, (e-s)*min(heights[s], heights[e]))
        if heights[s] < heights[e]:
            s += 1
        else:
            e -= 1
    return maxwater


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
