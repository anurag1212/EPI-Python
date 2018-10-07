from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    nums = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    res = []

    def recurse(word=[]):
        if len(word) == len(phone_number):
            res.append("".join(word))
            return
        for c in nums[int(phone_number[len(word)])]:
            word.append(c)
            recurse(word)
            word.pop()

    recurse()
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
