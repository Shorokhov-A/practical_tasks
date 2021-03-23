import os
from collections import defaultdict


def file_statistics(parent_dir):
    files_dict = defaultdict(list)
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            stat = os.stat(os.path.join(root, file))
            if stat.st_size <= 100:
                files_dict[100].append(file)
            elif stat.st_size <= 1000:
                files_dict[1000].append(file)
            elif stat.st_size <= 10000:
                files_dict[10000].append(file)
            else:
                files_dict[100000].append(file)
    result = {}
    for key, val in sorted(files_dict.items()):
        result[key] = len(val)
    return result


if __name__ == '__main__':
    print(file_statistics('some_data'))
