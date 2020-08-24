from luckyseven import Luckyseven
import random


# Parameters
b = 1
n = 10
mu = 6922
p = 10000
i = 5877
j = 80
l7 = Luckyseven()


# randomNumber = int(l7.prng(b, n, mu, i, j, p))
# # Print result
# print(randomNumber)

# ToBinary
# print(format(randomNumber, 'b').zfill(256))

sampleSize = 10**6

for sample in range(0, sampleSize):
    print(sample)
    mu = random.randint(0, 10**5)
    randomNumber = int(l7.prng(b, n, mu, i, j, p))
    binaryNumber = format(randomNumber, 'b').zfill(256)[:256]
    with open("data.luckyseven", "a") as datafile:
        datafile.write(f'{binaryNumber}\n')