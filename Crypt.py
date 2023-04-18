import math

source_text = "The quick brown fox jumps over the lazy dog"


def func_modern_text(source_text):
    flex_text = source_text
    full_root = math.ceil(math.sqrt(len(source_text)))
    if len(source_text) < full_root ** 2:
        for i in range(0, full_root ** 2 - len(source_text)):
            flex_text += " "
    return flex_text


modern_text = func_modern_text(source_text)

root_from_len_modern_text = round(math.sqrt(len(modern_text)))
matrix = [[0 for i in range(root_from_len_modern_text)] for j in range(root_from_len_modern_text)]

for j in range(0, root_from_len_modern_text):
    for i in range(0, root_from_len_modern_text):
        matrix[j][i] = modern_text[j * root_from_len_modern_text + i]

encrypted_text = ""

for m in range(0, len(matrix)):
    for n in range(0, len(matrix)):
        encrypted_text += matrix[n][m]

print(matrix)
print(encrypted_text)
print("hi1")
