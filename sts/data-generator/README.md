# Data generator

## datagenerator.py

Python script to generate the samples using the Luckyseven library and a rng.

## Parameters

There are some restrictions related to the values of the different parameters of Luckyseven. To enforce that the parameters are setted correctly, there are 5 of them that are static and 1 that is random, i.e. mu.

The parameters used as input for the Luckyseven CSPRNG. 

### Random
- mu = random.randint(0, 10**5)

### Static
- b = 1
- n = 10
- p = 10000
- i = 5877
- j = 80
