import main_app
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-dir1", required=True, default=None, type=str, help="First dir")
parser.add_argument("-dir2", required=True, default=None, type=str, help="Second dir")
parser.add_argument("-criterion", required=False, default=100, type=int, help="Criterion percent")
parser.add_argument("--bin", required=False, default=None, action="store_true", help="are files binary")

args = parser.parse_args()
for filename1 in os.listdir(args.dir1):
    fullpath1 = os.path.join(args.dir1, filename1)
    for filename2 in os.listdir(args.dir2):
        fullpath2 = os.path.join(args.dir2, filename2)
        if args.bin:
            file1 = open(fullpath1, "rb")
            file2 = open(fullpath2, "rb")
            mode = "b"
        else:
            file1 = open(fullpath1, "r")
            file2 = open(fullpath2, "r")
            mode = "s"
        per1, per2 = main_app.file_comparing(file1, file2, mode)

        if per1 >= args.criterion or per2 >= args.criterion:
            print(f"{fullpath1} - {fullpath2}")
        else:
            print(f"{fullpath1} - {fullpath2} - {min(per1, per2)*100:.2f}%")

