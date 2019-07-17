import ctypes
import time

def sumrange(a, b, c):
    someting = 0
    total    = 0
    for x in range(c):
        for y in range(c):
            someting += x*x + x*y + y
            total = x+y
    return total

if __name__ == "__main__":
    # Execute C code
    clib = ctypes.cdll.LoadLibrary("./c/main.so")
    clib.hello()
    print(clib.sum(5, 6))

    # Execute C++ code
    r = 100000
    cpplib = ctypes.cdll.LoadLibrary("./cpp/main.so")
    cpplib.hello()
    print(cpplib.sum(5, 6))

    t = time.clock()
    print("Sum: ", cpplib.sumrange(100, 100, r), end="")
    print(" - Time: {0:.3f} sec".format(time.clock() - t))
    t = time.clock()
    print("Sum: ", sumrange(100, 100, r), end="")
    print(" - Time: {0:.3f} sec".format(time.clock() - t))