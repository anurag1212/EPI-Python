from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    running_sum, total = 0, 0
    for t in sorted(service_times)[:-1]:
        running_sum += t
        total += running_sum
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
