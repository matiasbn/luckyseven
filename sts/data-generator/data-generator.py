from luckyseven import Luckyseven
import random


# Parameters
b = 1
n = 10
mu = random.randint(0, 10**5)
p = 10000
i = 5877
j = 80
l7 = Luckyseven()

sampleSize = 7*10**4

for sample in range(1, sampleSize):
    print(sample)
    mu = random.randint(0, 10**5)
    randomNumber = int(l7.prng(b, n, mu, i, j, p))
    binaryNumber = format(randomNumber, 'b').zfill(256)[:256]
    with open("data.luckyseven", "a") as datafile:
        datafile.write(f'{binaryNumber}\n')
