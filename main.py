# FACTOR FINDING

n = input("WHAT IS YOUR NUMBER!!!!!!")
factors = []
n = int(n)


for i in range(1, n, 1):
    if n % i == 0:
        factors.append(i)

factors.remove(1)
if len(factors) == 0:
    print("{} is a prime number (no factors except itself and 1)".format(n))
else:
    print("The factors of {} are {}".format(n, factors))
