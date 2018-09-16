from test_framework import generic_test
from collections import defaultdict
import copy

def num_combinations_for_final_score(final_score, individual_play_scores):

    class Path:
        def __init__(self):
            self.all_paths = []
            self._n = 0

        def add(self, incoming_path):
            if incoming_path not in self.all_paths:
                ip = copy.deepcopy(incoming_path)
                self.all_paths.append(ip)
                self._n += 1

        def __len__(self):
            return self._n

        def __bool__(self):
            return bool(self._n)

    DP = [Path() for _ in range(final_score+1)]

    def state(i):
        if i in individual_play_scores and i <= final_score:
            a = defaultdict(lambda: 0)
            a[i] += 1
            DP[i].add(a)
        if DP[i]:
            return DP[i]
        if i == 0:
            return None

        for score in individual_play_scores:
            prev_step = max(0, i-score)              # to handle bounds
            path_prefixes = state(prev_step)           # have to add score to all paths and try to add to my paths
            if path_prefixes:
                path_prefixes = path_prefixes.all_paths
                for p in path_prefixes:
                    temp = copy.deepcopy(p)
                    temp[score] += 1
                    DP[i].add(temp)                      # Try adding path to my paths
        return DP[i]

    state(final_score)
    # print(DP[-1].all_paths)
    return len(state(final_score))


# print(num_combinations_for_final_score(5, [2,3,7]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
