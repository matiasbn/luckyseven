# Statistical Test Suite

Here i'm going to write the results and it analysis.

## Original STS

Original STS code can be found [here](https://csrc.nist.gov/Projects/Random-Bit-Generation/Documentation-and-Software).

## Already executed tests

- [ ] Frecuency test

## Data generator

data-generator is a script that uses the Luckyseven library along with a rng to generate samples for statistical purposes.

## Luckyseven samples

data.luckyseven contains 70k samples of 256 "ASCII 0's or 1's" as a binary representation of the samples obtained through the data-generator script.

## Significance level

Significance level (alpha) is adjusted to 0.001. This means that is expected that 1/1000 samples is not considered a random sequence. This means that the sample size (m) should be greater or equal to 1/alpha = 1000.

## Frecuency test
