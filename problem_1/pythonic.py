__author__ = 'g42gregory'
import time

start = time.time()
max = 1000

sum = sum([i for i in range(max) if i % 3 == 0 or i % 5 == 0])

end = time.time()
print sum
print end - start