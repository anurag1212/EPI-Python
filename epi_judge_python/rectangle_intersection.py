import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    R3 = Rectangle(None, None, None, None)
    if R2.x <= R1.x <= R2.x + R2.width or R2.x <= R2.x + R2.width <= R2.x + R2.width:
        R3.x = R2.x if R2.x > R1.x else R1.x
    if R2.y <= R1.y <= R2.y + R2.height or R2.y <= R2.y + R2.height <= R2.y + R2.height:
        R3.y = R2.y if R2.y > R1.y else R1.y
    R3.height = min(R2.y + R2.height, R1.y + R1.height) - max(R2.y, R1.y)
    R3.width = min(R2.x + R2.width, R1.x + R1.width) - max(R2.x, R1.x)
    if R3.x is None or R3.y is None:
        return None
    return R3


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
