__author__ = 'g42gregory'
import time

start = time.time()

max = 4000000
sum = 2
f1 = 1
f2 = 2

while True:
    f3 = f1 + f2
    if f3 > max:
        break
    if f3 % 2 == 0:
        sum += f3
    f1 = f2
    f2 = f3
    #print f3

end = time.time()
print sum
print end - start