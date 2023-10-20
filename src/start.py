import main_app


f1 = open("f1", "rb")
f2 = open("f2", "rb")
print(main_app.file_comparing(f1, f2, "b"))

ff1 = open("ff1", "r")
ff2 = open("ff2", "r")
print(main_app.file_comparing(ff1, ff2, "s"))
