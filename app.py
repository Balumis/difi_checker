import hashlib

# sysalgorithms = hashlib.algorithms_available
# print("Dostepne algorithy na twoim systemie")
# for algo in sysalgorithms:
#     print(algo)

with open("new.docx", "rb") as f:
    file_hash = hashlib.sha256()
    while chunk := f.read(8192):
        file_hash.update(chunk)

print(file_hash.digest())
print(file_hash.hexdigest())  # to get a printable str instead of bytes
