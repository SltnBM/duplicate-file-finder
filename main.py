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


def handle_duplicates(dupes):
    for file1, file2 in dupes:
        print("\nDuplicate found:")
        print(f"1: {file1}")
        print(f"2: {file2}")

        while True:
            choice = input(
                "\nWhat do you want to do?\n"
                "1. Delete first file\n"
                "2. Delete second file\n"
                "3. Keep both files\n"
                "4. Skip\n"
                "Choose (1/2/3/4): "
            ).strip()

            if choice == "1":
                os.remove(file1)
                print("Deleted:", file1)
                break

            elif choice == "2":
                os.remove(file2)
                print("Deleted:", file2)
                break

            elif choice == "3":
                print("Keeping both files")
                break

            elif choice == "4":
                print("Skipped")
                break

            else:
                print("Invalid choice, try again.")


folder_path = input("Enter folder path to scan: ")
dupes = find_duplicates(folder_path)

if dupes:
    print("\nDuplicate files found:\n")

    for dup in dupes:
        print(f"{dup[0]} <==> {dup[1]}")

    confirm = input("\nDo you want to manage these duplicates now? (y/n): ").lower()

    if confirm == "y":
        handle_duplicates(dupes)

else:
    print("No duplicate files found.")