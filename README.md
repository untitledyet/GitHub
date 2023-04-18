# Symmetric Encryption - Matrix Approach

Overview:
Symmetric encryption is a method of encryption where the same key is used for both encryption and decryption. In this matrix approach, a matrix (list by list) is created based on the length of the input text. If the square root of the length of the input text is not an integer, the matrix is padded with blank spaces until the square root becomes an integer. The input text is then written into the matrix by filling the rows and columns sequentially.

Encryption Process:

Create a matrix (list by list) based on the length of the input text.
If the square root of the length of the input text is not an integer, pad the matrix with blank spaces until the square root becomes an integer.
Write the input text into the matrix by filling the rows and columns sequentially, starting from the top left corner of the matrix.
Read the first character from each list in the matrix, and concatenate them to get the encrypted text.
Decryption Process:

Create a matrix (list by list) based on the length of the encrypted text.
If the square root of the length of the encrypted text is not an integer, pad the matrix with blank spaces until the square root becomes an integer.
Write the encrypted text into the matrix by filling the columns sequentially, starting from the top left corner of the matrix.
Read the characters from the matrix row-wise to get the decrypted text.
Example:
Input Text: "The quick brown fox jumps over the lazy dog"
Matrix:
[['T', 'h', 'e', ' ', 'q', 'u', 'i'],
['c', 'k', ' ', 'b', 'r', 'o', 'w'],
['n', ' ', 'f', 'o', 'x', ' ', 'j'],
['u', 'm', 'p', 's', ' ', 'o', 'v'],
['e', 'r', ' ', 't', 'h', 'e', ' '],
['l', 'a', 'z', 'y', ' ', 'd', 'o'],
['g', ' ', ' ', ' ', ' ', ' ', ' ']]
Encrypted Text: "Tcnuelghk mra e fp z bosty qrx h uo oed iwjv o "

Note: The same process can be used to encrypt the already encrypted text (i.e., perform encryption iteratively), by treating the encrypted text as the input text for the next round of encryption.

That's it! This is how the symmetric encryption using the matrix approach works.
