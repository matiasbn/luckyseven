from luckyseven import Luckyseven

# Parameters
b = 1
n = 8
mu = 7192
p = 10000
i = 5877
j = 200

l7 = Luckyseven()

# Print result
print(l7.prng(b, n, mu, i, j, p))
