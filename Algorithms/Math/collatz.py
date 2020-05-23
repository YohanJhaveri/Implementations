collatz_dict = {}

def collatz(n):
    sequence = []
    x = n
    while x != 1:
        sequence.append(x)
        if x%2 == 0:
            x //= 2
        else:
            x = (3 * x) + 1
        if x in collatz_dict:
            collatz_dict[n] = sequence + collatz_dict[x]
            return collatz_dict[n]
    collatz_dict[n] = sequence + [1]
    return collatz_dict[n]



import time

start = time.time()
for x in range(1, 10000000):
    str(x) + ':' + str(collatz(x))
end = time.time()

print(end - start)

# print(collatz_dict)
