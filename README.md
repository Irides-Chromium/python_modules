# python modules
This repo includes some useful python modules that can be used in development.

## The scale module
This module is used to convert numbers of different scales (bases, such as 2 for binary or 16 for hexadecimal). The supporting bases is up to 62 with all numbers and letters (including capitals). For bases larger than 36, capital letters are used to represent bigger numbers, like 'A' would represent 36. For bases smaller than 36, capital and non-capital letters are the same.


For the function parameters, `cur` represents the current (input) base, `res` represents the result (output) base, and `num` represents the current (input) number.

## The putchar module
This module is for Python3. Python3 uses Unicode for encoding, so printing character in ascii for encoding is a little bit hard. It just use the C properties so that the characters would print properly.
