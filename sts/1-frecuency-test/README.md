# Frecuency test

The focus of the test is the proportion of zeroes and ones for the entire sequence. The purpose of this test
is to determine whether the number of ones and zeros in a sequence are approximately the same as would
be expected for a truly random sequence. The test assesses the closeness of the fraction of ones to ½, that
is, the number of ones and zeroes in a sequence should be about the same. All subsequent tests depend on
the passing of this test. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: bits length
- m: amount of bit streams (or samples)

## Values

- n: 256
- m: 5000

# Results

```
The minimum pass rate for each statistical test with the exception of the random excursion (variant) test is approximately = 4988 for a
sample size = 5000 binary sequences.
```

Being the proportion equal to 4998/5000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
