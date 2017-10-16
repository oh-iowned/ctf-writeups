# Hack Dat Kiwi 2017
## PS1

## Information
**Category:** | **Points:** | **Author:**
--- | --- | ---
Crypto | 100 | Ben Burnett

## Description
We are presented with a php script responsible for encryption and decryption along with three parameters for configuring it:
```
BLOCK_SIZE = 16;
SEED = 1396;
ROUNDS = 1;
```

We are presented with a large block of ciphertext, and asked to decrypt it.

## Solution
The first thing I did was an analysis of the php encryption script. The variable `ROUNDS` from earlier refers to how many passes of encryption would take place.
Each pass puts the plaintext through `sbox`, `pbox`, and `xbox`.

#### sbox
This is a simple substitution box. Based on the SEED, the numbers from 0-255 are randomized and assigned as values to the keys 0-255 in a dictionary. When the `sbox` processes it looks up the ordinal of the plaintext character in this dictionary and substitutes the value.

#### pbox
This is a permutation box. Based on the SEED, an array of the numbers 0-15 is randomized. This array represents the order in which the block will be rearranged.

#### xbox
A simple xor. It is taking the block, and xoring it with the md5 hash of the key.

Based on this information, and that only one ROUND takes place, I decided that I wanted to try and recover the md5 of the key.
To do this, we can ignore the `pbox` as the xor takes place afterwards.
The idea is that we block off the ciphertext in to BLOCKSIZE blocks, and then columnize the blocks. Columnize meaning that we take index 0 of every block and put that in to a new list. We repeat that process for each index.
What we know now is that each column was xored with the same key character, so we write a script to test all valid numbers that could have been xored with our ciphertext that when put through the `sbox` backwards results in printable ascii. We then find the intersect of the solutions for each character in a column, and see what falls out. In this case, our output was:

```
['0xf2']
['0x76']
['0x14']
['0xc5']
['0x21']
['0xa']
['0x17']
['0x4d']
['0xa7']
['0x92']
['0xe9']
['0x2']
['0x86']
['0x6b']
['0xd7']
['0x40']
```

So we pieced back together the md5 `f27614c5210a174da792e902866bd740`, plugged it in to the php script, and decoded the message.


