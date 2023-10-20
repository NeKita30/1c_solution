from diff_match_patch import diff_match_patch
import typing


def file_comparing(file1: typing.IO, file2: typing.IO, mode) -> (float, float):
    content1 = file1.read()
    content2 = file2.read()

    model = diff_match_patch()

    equality = 0

    if mode == "b":
        diff = model.diff_main(content1.hex(" "), content2.hex(" "))
        equality = __compute_equality_bytes(diff)
    elif mode == "s":
        diff = model.diff_main(content1, content2)
        equality = __compute_equality_str(diff)

    return equality / len(content1), equality / len(content2)


def __compute_equality_str(diff: list[tuple[int, str]]) -> int:
    equality_cnt = 0
    for code, word in diff:
        cnt = len(word)
        if code == 0:
            equality_cnt += cnt
    return equality_cnt


def __compute_equality_bytes(diff: list[tuple[int, str]]) -> int:
    equality_cnt = 0
    for code, bytes_str in diff:
        bits = bytes_str.split()
        if code == 0:
            if len(bits) > 0 and len(bits[0]) < 2:
                bits.pop(0)
            if len(bits) > 0 and len(bits[-1]) < 2:
                bits.pop(-1)
            equality_cnt += len(bits)
    return equality_cnt
