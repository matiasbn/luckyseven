# Frequency Test within a Block

The focus of the test is the proportion of ones within M-bit blocks. The purpose of this test is to determine
whether the frequency of ones in an M-bit block is approximately M/2, as would be expected under an
assumption of randomness. For block size M=1, this test degenerates to test 1, the Frequency (Monobit)
test. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: bits length
- m: amount of bit streams (or samples)
- M: block size

## Values

- n: 256
- m: 5000
- M: 128

# Results

```
The minimum pass rate for each statistical test with the exception of the
random excursion (variant) test is approximately = 4988 for a
sample size = 5000 binary sequences.
```

Being the proportion equal to 4994/5000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
