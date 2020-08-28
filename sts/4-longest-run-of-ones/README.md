# Test for the Longest Run of Ones in a Block

The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to determine whether the length of the longest run of ones within the tested sequence is consistent with the length of the longest run of ones that would be expected in a random sequence. Note that an irregularity in the expected length of the longest run of ones implies that there is also an irregularity in the expected length of the longest run of zeroes. Therefore, only a test for ones is necessary. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: bits length
- m: amount of bit streams (or samples)
- M: the length of each block

## Values

- n: 256
- m: 5000
- M: n < 6272 => 8

# Results

```
The minimum pass rate for each statistical test with the exception of the
random excursion (variant) test is approximately = 4988 for a
sample size = 5000 binary sequences.
```

Being the proportion equal to 4995/5000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
