# 1c_solution
1С отбор на кафедру

### ФИО:
Чубарев Никита Константинович 
### Задача:
Задача №4
### Запуск решения
Нужно запустить файл `src/start.py`, передав нужные аргументы:

```usage: start.py [-h] -dir1 DIR1 -dir2 DIR2 [-criterion CRITERION] [--bin]

options:
  -h, --help            show this help message and exit
  -dir1 DIR1            First dir
  -dir2 DIR2            Second dir
  -criterion CRITERION  Criterion percent
  --bin                 are files binary
```
Пример:
python3 src/start.py -dir1 path1 -dir2 path2 --bin -criterion=30

### Проектные решения
Используется реализованный [Myer's diff algorithm](https://neil.fraser.name/writing/diff/myers.pdf).

В `src` находится файл `diff_match_patch.py`, взятый из [репозитория](https://github.com/google/diff-match-patch/tree/master).

Проект написан на `Python`.


