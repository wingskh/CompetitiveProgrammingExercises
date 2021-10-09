import time
import random

s = [random.randint(0, 1) for _ in range(10000000)]

start_time = time.time()
zero_counter = 0
one_counter = 0
for c in s:
    if c == "0":
        zero_counter += 1
    else:
        one_counter += 1
print("Excution Time:", time.time() - start_time)


zero_counter = s.count("0")
one_counter = len(s) - zero_counter
start_time = time.time()
print("Excution Time:", time.time() - start_time)

zero_counter = s.count("0")
one_counter = s.count("1")
start_time = time.time()
print("Excution Time:", time.time() - start_time)
