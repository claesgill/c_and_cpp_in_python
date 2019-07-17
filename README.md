# Executing C and C++ code in Python!
Testing functions made in _C_ and _C++_ in _Python_ and _JavaScript_ using the ``ctypes``and ``ffi`` libraries.
The _C_ and _C++_ files are compiled into a ``shared object file`` that the libraries require.

The ``sumrange()``-function is identical made in both _C++_ and Python to test execution time. Setting ``r=100000`` resulted in **25 seconds** execution time for _C++_, and **32 minutes** for _Python_! So if you need to calculate something fast within _Python_, this could be a good solution.

### Compiling in terminal
__C code:__  
```gcc -c -fPIC main.c -o main.o``` creates an object file.  

```gcc main.o -shared -o main.so``` creates an shared object file.

__C++ code:__  
```g++ -c -fPIC main.cpp -o main.o``` creates an object file.
```g++ main.o -shared -o main.so``` creates an shared object file.

### System
MacOS  
Python 3.6.4