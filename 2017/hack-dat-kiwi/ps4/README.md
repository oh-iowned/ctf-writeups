# Hack Dat Kiwi 2017
## PS4

## Information
**Category:** | **Points:** | **Author:**
--- | --- | ---
Crypto | 120 | Ben Burnett

## Description
We are presented with a php script responsible for encryption and decryption along with three parameters for configuring it:
```
BLOCK_SIZE = 16;
SEED = 999999;
ROUNDS = 4;
```

We are presented with a large block of ciphertext, and asked to decrypt it.

This is the same encryption script that PS1 and PS2 use, but the parameters are different. Most interestingly the encryption goes through four rounds.

## Solution
I don't want to repeat too much from the PS1 or PS2 write-up, so I'll assume that you have read that one first.
Again, the major difference here is that the encryption goes through four passes.
This means that each piece of cipher text is encrypted by four, probably different, pieces of the key.

The plan of attack here is to use the solution for PS2 but scale it to run two more loops.
Obviously we can't do 256^4 solutions for each character of ciphertext so we make some optimizations.
* We look to start with a column that reuses part of the key. This reduces the space to 256^3.
* Once we solve a character in a column we feed that reduced solution set in to the next character instead of doing 256^3 for each character.
* Once we solve a column we reuse those solved key components to speed up the solves of the remaining columns.

You will find the complete script in `ps4.py`. It does take a bit to calculate the first column, but in the end you get the following output after solving only 8/16 columns:
```
0	= k[0]	k[3]	k[14]	k[12]
1	= k[1]	k[11]	k[6]	k[5]
2	= k[2]	k[15]	k[0]	k[2]
3	= k[3]	k[10]	k[11]	k[15]
4	= k[4]	k[2]	k[1]	k[9]
5	= k[5]	k[6]	k[15]	k[10]
6	= k[6]	k[14]	k[10]	k[3]
7	= k[7]	k[9]	k[13]	k[4]
8	= k[8]	k[7]	k[4]	k[8]
9	= k[9]	k[0]	k[8]	k[11]
10	= k[10]	k[12]	k[3]	k[7]
11	= k[11]	k[5]	k[2]	k[13]
12	= k[12]	k[4]	k[12]	k[14]
13	= k[13]	k[8]	k[7]	k[1]
14	= k[14]	k[13]	k[9]	k[0]
15	= k[15]	k[1]	k[5]	k[6]
Solving column 12 ...
Solves 0: 6619136
Solves 1: 2593480
Solves 2: 1011669
Solves 3: 390933
Solves 4: 150284
Solves 5: 57409
Solves 6: 21847
Solves 7: 8343
Solves 8: 8343
Solves 9: 8343
Solves 10: 3166
Solves 11: 1160
Solves 12: 1160
Solves 13: 409
Solves 14: 409
Solves 15: 409
Solves 16: 157
Solves 17: 157
Solves 18: 157
Solves 19: 50
Solves 20: 13
Solves 21: 4
Solves 22: 4
Solves 23: 2
Solves 24: 1
Solving column 0 ...
Solves 0: 25856
Solves 1: 10180
Solves 2: 3967
Solves 3: 1569
Solves 4: 1569
Solves 5: 1569
Solves 6: 633
Solves 7: 633
Solves 8: 633
Solves 9: 243
Solves 10: 243
Solves 11: 83
Solves 12: 35
Solves 13: 10
Solves 14: 10
Solves 15: 10
Solves 16: 10
Solves 17: 10
Solves 18: 10
Solves 19: 10
Solves 20: 10
Solves 21: 4
Solves 22: 4
Solves 23: 4
Solves 24: 4
Solves 25: 1
Solving column 6 ...
Solves 0: 25856
Solves 1: 9900
Solves 2: 3777
Solves 3: 3777
Solves 4: 1434
Solves 5: 552
Solves 6: 219
Solves 7: 101
Solves 8: 101
Solves 9: 101
Solves 10: 34
Solves 11: 34
Solves 12: 12
Solves 13: 12
Solves 14: 12
Solves 15: 5
Solves 16: 3
Solves 17: 3
Solves 18: 3
Solves 19: 2
Solves 20: 2
Solves 21: 2
Solves 22: 2
Solves 23: 1
Solving column 5 ...
Solves 0: 25856
Solves 1: 10136
Solves 2: 4016
Solves 3: 1572
Solves 4: 609
Solves 5: 255
Solves 6: 92
Solves 7: 30
Solves 8: 30
Solves 9: 15
Solves 10: 15
Solves 11: 15
Solves 12: 15
Solves 13: 15
Solves 14: 4
Solves 15: 3
Solves 16: 3
Solves 17: 3
Solves 18: 3
Solves 19: 3
Solves 20: 1
Solving column 1 ...
Solves 0: 25856
Solves 1: 10172
Solves 2: 10172
Solves 3: 4124
Solves 4: 4124
Solves 5: 4124
Solves 6: 1645
Solves 7: 1645
Solves 8: 1645
Solves 9: 662
Solves 10: 662
Solves 11: 264
Solves 12: 100
Solves 13: 100
Solves 14: 100
Solves 15: 100
Solves 16: 100
Solves 17: 40
Solves 18: 40
Solves 19: 40
Solves 20: 15
Solves 21: 5
Solves 22: 5
Solves 23: 2
Solves 24: 2
Solves 25: 2
Solves 26: 1
Solving column 2 ...
Solves 0: 25856
Solves 1: 10184
Solves 2: 10184
Solves 3: 3883
Solves 4: 1418
Solves 5: 519
Solves 6: 519
Solves 7: 519
Solves 8: 519
Solves 9: 225
Solves 10: 225
Solves 11: 225
Solves 12: 84
Solves 13: 26
Solves 14: 12
Solves 15: 6
Solves 16: 3
Solves 17: 3
Solves 18: 3
Solves 19: 3
Solves 20: 2
Solves 21: 2
Solves 22: 2
Solves 23: 1
Solving column 9 ...
Solves 0: 25856
Solves 1: 10276
Solves 2: 4086
Solves 3: 1557
Solves 4: 590
Solves 5: 590
Solves 6: 590
Solves 7: 590
Solves 8: 215
Solves 9: 215
Solves 10: 98
Solves 11: 32
Solves 12: 10
Solves 13: 4
Solves 14: 1
Solving column 7 ...
Solves 0: 25856
Solves 1: 10268
Solves 2: 4054
Solves 3: 1606
Solves 4: 636
Solves 5: 237
Solves 6: 237
Solves 7: 237
Solves 8: 237
Solves 9: 88
Solves 10: 88
Solves 11: 33
Solves 12: 13
Solves 13: 7
Solves 14: 7
Solves 15: 7
Solves 16: 7
Solves 17: 7
Solves 18: 7
Solves 19: 2
Solves 20: 2
Solves 21: 2
Solves 22: 2
Solves 23: 2
Solves 24: 2
Solves 25: 2
Solves 26: 2
Solves 27: 2
Solves 28: 2
Solves 29: 1
md5 = 83fd68205d7e294be2267fe68a2850d3
```
And we can use the md5 `83fd68205d7e294be2267fe68a2850d3` in the php script to decrypt the message.


