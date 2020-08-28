# Test for the Longest Run of Ones in a Block

The focus of the test is the rank of disjoint sub-matrices of the entire sequence. The purpose of this test is to check for linear dependence among fixed length substrings of the original sequence. Note that this test also appears in the DIEHARD battery of tests. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: bits length
- m: amount of bit streams (or samples)

## Values

- n: 38912
- m: 4000

# Results

```
The minimum pass rate for each statistical test with the exception of the
random excursion (variant) test is approximately = 3990 for a
sample size = 4000 binary sequences.
```

Being the proportion equal to 3997/4000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
