from diff_match_patch import diff_match_patch
import typing


def file_comparing(file1: typing.BinaryIO, file2: typing.BinaryIO) -> str:
    content1 = file1.read()
    content2 = file2.read()
    len_1 = len(content1)
    len_2 = len(content2)
    if len_1 < len_2:
        len_1, len_2 = len_2, len_1
        content1, content2 = content2, content1

    model = diff_match_patch()

    diff = model.diff_main(str(content1), str(content2))
    return diff


def __compute_percent(diff: list[tuple[int, bytes]]):
    pass
