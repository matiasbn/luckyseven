# Test for the Longest Run of Ones in a Block

The focus of this test is the number of occurrences of pre-specified target strings. The purpose of this test is to detect generators that produce too many occurrences of a given non-periodic (aperiodic) pattern. For this test and for the Overlapping Template Matching test of Section 2.8, an m-bit window is used to search for a specific m-bit pattern. If the pattern is not found, the window slides one bit position. If the pattern is found, the window is reset to the bit after the found pattern, and the search resumes. [[1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf)]

# Parameters

This are the values of non-default parameters.

## Names

- n: The length of the entire bit string under test.
- m: The length in bits of each template. The template is the target string.
- b: amount of bit streams

## Values

- n: 4096
- m: 9
- b: 5000

# Results

```
The minimum pass rate for each statistical test with the exception of the
random excursion (variant) test is approximately = 4988 for a
sample size = 5000 binary sequences.
```

Being the proportion equal to 4991/5000 [result/finalAnalysisReport.txt], this test can be considered as PASSED.
