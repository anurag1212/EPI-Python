from test_framework import generic_test


def multiply(x, y):
    def add(n1, n2):
        carryin, t1, t2, k, rsum = 0, n1, n2, 0, 0
        while t1 or t2:
            ak = n1 & k
            bk = n2 & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            rsum |= ak ^ bk ^ carryin
            carryin = carryout << 1
            k <<= 1
            t1 >>= 1
            t2 >>= 1
        rsum |= carryin
        return rsum

    r_sum = 0
    while x:
        if x & 1:
            r_sum = add(r_sum, y)
        x >>= 1
        y <<= 1
    return r_sum


def multiply_old(x, y):

    def add(num1, num2):
        running_sum, k, ta, tb, carryin = 0, 1, num1, num2, 0
        while ta or tb:
            b1 = num1 & k
            b2 = num2 & k
            carryout = b1 & b2 | b1 & carryin | b2 & carryin
            running_sum |= b1 ^ b2 ^ carryin
            carryin = carryout << 1
            ta, tb = ta >> 1, tb >> 1
            k <<= 1
        return running_sum | carryin

    rsum = 0
    while x:
        if x & 1:
            rsum = add(rsum, y)
        x >>= 1
        y <<= 1

    return rsum


# I give up, too fiddly
def adder(num1, num2):
    mask = 1
    carry = 0
    ta, tb = num1, num2
    print("num1: {0:b}   num2: {1:b}".format(num1, num2))
    while ta or tb:
        b1 = num1 & mask
        b2 = num2 & mask
        b1 = (b1 ^ (b1-1)) & 1
        b2 = (b2 ^ (b2-1)) & 1
        print("Mask   {0:b}".format(mask))
        print("b1: {0:b}     b2: {1:b}".format(b1, b2))
        if b1 & b2 & carry:
            bit, carry = 1, 1
        elif b1 & b2 or b1 & carry or b2 & carry:
            bit, carry = 0, 1
        elif b1 | b2 | carry:
            bit, carry = 1, 0
        else:
            bit, carry = 0, 0
        print("Bit {0} carry {1}".format(bit, carry))
        if ((num1 & mask) >> (mask >> 1)) ^ bit:
            print("Before {0:b}".format(num1))
            num1 ^= mask
            print("After  {0:b}".format(num1))
        mask <<= 1
        ta >>= 1
        tb >>= 1
        print()
    return num1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
