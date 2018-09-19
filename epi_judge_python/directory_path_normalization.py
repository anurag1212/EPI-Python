from test_framework import generic_test


def shortest_equivalent_path(path):
    path = path.split("/")
    stk = []
    curr = 0
    while curr < len(path):
        e = path[curr]
        if e == "..":
            if stk:
                if stk[-1] != "..": stk.pop()
                else: stk.append("..")
            else:
                stk.append("..")
        elif e == ".": pass
        elif not e: pass
        else: stk.append(e)
        curr += 1

    return "/" + "/".join(stk) if not path[0] else "/".join(stk)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
