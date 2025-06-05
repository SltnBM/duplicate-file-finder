import os
import hashlib

def hash_file(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(folder):
    files = {}
    duplicates = []

    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(root, filename)
            file_hash = hash_file(path)
            if file_hash in files:
                duplicates.append((path, files[file_hash]))
            else:
                files[file_hash] = path

    return duplicates

folder_path = input("Enter folder path to scan: ")
dupes = find_duplicates(folder_path)

if dupes:
    print("Duplicate files found:")
    for dup in dupes:
        print(f"{dup[0]} <==> {dup[1]}")
else:
    print("No duplicate files found.")
