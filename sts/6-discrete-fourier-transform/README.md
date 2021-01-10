# Test for the Longest Run of Ones in a Block

The focus of this test is the peak heights in the Discrete Fourier Transform of the sequence. The purpose of this test is to detect periodic features (i.e., repetitive patterns that are near each other) in the tested sequence that would indicate a deviation from the assumption of randomness. The intention is to detect whether the number of peaks exceeding the 95 % threshold is significantly different than 5 %. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: bits length
- m: amount of bit streams (or samples)

## Values

- n: 4096
- m: 5000

# Results

```
The minimum pass rate for each statistical test with the exception of the
random excursion (variant) test is approximately = 4988 for a
sample size = 5000 binary sequences.
```

Being the proportion equal to 4991/5000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
