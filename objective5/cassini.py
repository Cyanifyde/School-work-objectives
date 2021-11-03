"""
The Cassini-Huygens spacecraft that visited the planet Saturn had 2.5Gb of memory. Due to solar particles hitting the spacecraft, the memory frequently became corrupted. In its first 2 years alone it suffered 280 single-bit errors on average every day. Without a method of detecting and correcting bits flipping between the zero and one state the spacecraft would be useless. One such method of detecting errors is odd parity. A sequence of bits must contain an odd number of ones and an additional bit is included in the data to ensure this. E.g.
0110001 0 contains three ones (including the parity bit which is set to 0). This sequence is correct.
0110011 0 contains four ones (including the parity bit which is set to 0). This sequence is incorrect and must be corrected.
Write a function called, “OddParity” that takes a binary sequence as a parameter and returns True if the number of ones is odd and False if the number of ones is even.
"""
def OddParity(sequence):
    count=sequence.count("1")
    if (count % 2) != 0:
        return True
    else:return False
print("correct" if OddParity(input()) else "incorrect")
