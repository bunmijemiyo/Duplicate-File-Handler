
import os
import argparse
import hashlib
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="Enter a file directory", nargs="?")
args = parser.parse_args()
file_dict = {}
hash_dict = {}
choice_box = {}
delete_size = []
if args.file:
    file_type = input("Enter file format:\n")
    print("\nSize sorting options:\n1. Descending\n2. Ascending")
    for root, dirs, files in os.walk(args.file):
        for name in files:
            file_name, file_ext = os.path.splitext(os.path.join(root, name))
            if file_ext == f'.{file_type}' or file_type == '':
                size = os.path.getsize(os.path.join(root, name))
                if size in file_dict.keys():
                    file_dict[size].append(os.path.join(root, name))
                else:
                    file_dict[size] = [os.path.join(root, name)]
    while True:
        print("Enter a sorting option:")
        sort_option = input()
        if sort_option in ['1', '2']:
            break
        else:
            print('Wrong option')
    if sort_option == "2":
        sort_option = False
    elif sort_option == "1":
        sort_option = True
    for k, v in sorted(file_dict.items(), reverse=sort_option):
        print(f"\n{k} bytes")
        for i in v:
            print(i)
else:
    print("Directory is not specified")

duplicate_choice = input().lower()
while True:
    if duplicate_choice == "yes":
        break
    else:
        continue

for k, v in sorted(file_dict.items()):
    hash_dict[k] = []
    for i in v:
        with open(i, "rb") as hash_file:
            content = hash_file.read()
            md5_file = hashlib.md5()
            md5_file.update(content)
            result = md5_file.hexdigest()
            for index in range(len(hash_dict[k])):
                if result in hash_dict[k][index]:
                    hash_dict[k][index].append(i)
            else:
                hash_dict[k].append([])
                hash_dict[k][-1].append(result)
                hash_dict[k][-1].append(i)

count = []
for k, v in sorted(hash_dict.items(), reverse=sort_option):
    print()
    print(k, "bytes")
    for i in range(len(hash_dict[k])):
        if len(hash_dict[k][i]) > 2:
            for num in range(len(hash_dict[k][i])):

                if num == 0:
                    print("Hash:", hash_dict[k][i][num])
                else:
                    count.append(1)
                    choice_box[sum(count)] = []
                    choice_box[sum(count)].append(hash_dict[k][i][num])
                    choice_box[sum(count)].append(k)
                    print(f"{sum(count)}. {hash_dict[k][i][num]}")

while True:
    delete_files = input("Delete files?\n").lower()
    if delete_files == "yes":
        break
    elif delete_files == "no":
        sys.exit()
    else:
        print("Wrong option")

while True:
    file_to_delete = input("Enter file numbers to delete:\n")
    if len(file_to_delete) == 0:
        print("Wrong format")
    else:
        choice = [str(i) for i in choice_box.keys()]
        box = [num for num in file_to_delete.split() if num in choice]
        if len(box) == len(file_to_delete.split()):
            for values in file_to_delete.split():
                os.remove(choice_box[int(values)][0])
                #os.rmdir(choice_box[int(values)][0])
                delete_size.append(choice_box[int(values)][1])
            print(f"\nTotal freed up space: {sum(delete_size)} bytes")
            sys.exit()
        else:
            print("Wrong format")
