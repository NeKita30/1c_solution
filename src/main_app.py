from diff_match_patch import diff_match_patch
import typing


def file_comparing_str(file1: typing.TextIO, file2: typing.TextIO) -> (float, float):
    content1 = file1.read()
    content2 = file2.read()

    model = diff_match_patch()

    diff = model.diff_main(content1, content2)
    diff = model.diff_main(content1, content2)
    delete, insert, equal = __compute_fractions_str(diff)
    return equal / (delete + equal), equal / (insert + equal)


def __compute_fractions_str(diff: list[tuple[int, str]]) -> (int, int, int):
    equality_cnt = 0
    deletion_cnt = 0
    insertion_cnt = 0
    for code, bytes_str in diff:
        cnt = len(bytes_str)
        if code == 0:
            equality_cnt += cnt
        if code == 1:
            insertion_cnt += cnt
        if code == -1:
            deletion_cnt += cnt
    return deletion_cnt, insertion_cnt, equality_cnt

