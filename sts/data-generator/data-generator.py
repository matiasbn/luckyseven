import os
import random

from luckyseven import Luckyseven

# Parameters
b = 1
n = 10
p = 10000
j = 1250
i = random.randint(0, 100)
mu = random.randint(0, 100000)

l7 = Luckyseven()

filesPrefix = 'data.luckyseven'
files = os.listdir('..')
for file in files:
    if file.startswith(filesPrefix):
        os.remove(os.path.join('..', file))

child = 0
children = []
for process in range(2):
    print(process)
    child = os.fork()
    if child:
        children.append(child)

id = random.randint(0, 10000)

sampleSize = 10000
# print(sampleSize)
streamLength = 4096

for sample in range(0, sampleSize):
    print(sample)
    i = random.randint(0, 100)
    mu = random.randint(0, 100000)
    randomNumber = int(l7.prng(b, n, mu, i, j, p))
    binaryNumber = format(randomNumber, 'b').zfill(streamLength)[:streamLength]
    with open(f'../{filesPrefix}-{id}', "a") as datafile:
        datafile.write(f'{binaryNumber}\n')

for child in children:
    try:
        os.waitpid(child, 0);
    except:
        pass;

# Only parent process

files = os.listdir('..')
with open('../data', 'w') as outfile:
    for file in files:
        if file.startswith(filesPrefix):
            with open(f'../{file}') as infile:
                outfile.write(infile.read())
            os.remove(os.path.join('..', file))

os.rename(r'../data', fr'../{filesPrefix}')
