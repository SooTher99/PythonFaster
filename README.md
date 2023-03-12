**Команды для запуска**

Чистый Python:

* ```time python pure_python/main.py```

Сython:

* Для запуска без явной компиляции 
```time python pure_python/main.py```
* Компиляция ```python cython_exp/setup.py build_ext --inplace```

Numba:

* ```time python numba_exp/main.py```

Pypy:

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