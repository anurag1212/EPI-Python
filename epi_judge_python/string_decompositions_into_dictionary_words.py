from test_framework import generic_test
from collections import defaultdict


def find_all_substrings(s, words):
    dic, n, word_size, res = defaultdict(lambda: 0), len(words), len(words[0]), []
    while words:
        dic[words.pop()] += 1

    for i in range(0, len(s) - word_size + 1):
        start = i
        while start <= len(s) - word_size:
            curr_word = s[start:start+word_size]
            if dic[curr_word]:
                dic[curr_word] -= 1
                start += word_size
                n -= 1
                if not n:
                    res.append(i)
                    break
            else:
                dic.pop(curr_word)
                break

        j = i
        while j < start:
            n += 1
            dic[s[j:j+word_size]] += 1
            j += word_size
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
