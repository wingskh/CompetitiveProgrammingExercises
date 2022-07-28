file_a = {"id": 0, "size": 5, "type": "file", "child": [], "name": "file_a"}
file_b = {"id": 1, "size": 6, "type": "file", "child": [], "name": "file_b"}
file_c = {"id": 2, "size": 7, "type": "file", "child": [], "name": "file_c"}
dir_a = {"id": 4, "type": "dir", "child": [0, 5], "name": "folder_a"}
dir_b = {"id": 5, "type": "dir", "child": [1, 2], "name": "folder_b"}

mapping_table = {
    0: file_a,
    1: file_b,
    2: file_c,
    4: dir_a,
    5: dir_b,
}

files = [file_a, file_b, file_c, dir_a, dir_b]


def find_file_size(file):
    if file["type"] == "file":
        return file["size"]
    if "size" not in file:
        file["size"] = 0
    for i in file["child"]:
        file["size"] += find_file_size(mapping_table[i])

    return file["size"]


def print_file_system(file, level):
    print("   " * level + f"{file['name']} ({file['size']}mb)")
    if file["type"] == "dir":
        for child in file["child"]:
            print_file_system(mapping_table[child], level + 1)


total_set = set(list(mapping_table.keys()))

for file in files:
    for child in file["child"]:
        total_set.remove(child)

root = total_set.pop()
find_file_size(mapping_table[root])
print_file_system(mapping_table[root], 0)
