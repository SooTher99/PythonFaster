**Cython** позволяет писать программы, выглядящие почти как на python, 
но с добавлением статических деклараций типов. Эти программы c расширением "pyx"
транслируются в исходные тексты на C и затем компилируются.
Определённые в них функции могут использоваться из программ на чистом python. 

**Numba** переводит функции Python в оптимизированный машинный код 
во время выполнения, используя компилятор LLVM.

**PyPy** — интерпретатор, который является оптимизированным альтернативой CPython.

**Команды для запуска:**

Чистый Python:

* ```time python pure_python/main.py```

Сython:

* Для запуска без явной компиляции 
```time python pure_python/main.py```
* Компиляция ```python cython_exp/setup.py build_ext --inplace```

Numba:

* ```time python numba_exp/main.py```

PyPy:

Установка

```
cd /home/

wget https://downloads.python.org/pypy/pypy3.9-v7.3.11-linux64.tar.bz2

tar -xvf pypy3.9-v7.3.11-linux64.tar.bz2

/home/pypy3.9-v7.3.11-linux64/bin/pypy -V
```
Создание виртуального окружения 
```
/home/pypy3.9-v7.3.11-linux64/bin/pypy -m venv pypy-venv

. pypy-venv/bin/activate

pypy -mpip install -U pip wheel
```
Для запуска используйте туже команду, что и для чистого Python.

**Тесты производительности:**

|                  | Pure Python | Cython (не явная компиляция) | Cython (явная компиляция) | PyPy | Numba |
|------------------|-------------|------------------------------|---------------------------|------|-------|
| Время (секундны) | 4.011       | 1.276                        | 1.134                     | 0.17 | 0.04  |