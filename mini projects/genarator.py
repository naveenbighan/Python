import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
 time.sleep(3)
 return n*5
    

print(fx(5))
print(fx(10))
print(fx(15))
print(fx(75))
print(fx(52))
print(fx(51))
print(fx(59))


print(fx(5))
print(fx(10))
print(fx(15))
print(fx(75))
print(fx(52))
print(fx(51))
print(fx(59))