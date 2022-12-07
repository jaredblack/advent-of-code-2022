from collections import defaultdict
import math


in_file = open('in/day7.txt')
st = in_file.read()
in_file.close()

# Possible edge: repeated directory names, weird traversal

class Directory:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.subdirs = []
        self.parent = parent

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def get_subdir(self, name):
        for subdir in self.subdirs:
            if subdir.name == name:
                return subdir
        return None

    def get_size(self):
        if self.size == 0:
            return sum([x.get_size() for x in self.subdirs])
        else:
            return self.size

    def __str__(self):
        return self.name + " " + str(self.size)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return self.name + " " + str(self.size)

curr_path = []
root_dir = Directory("/", 0, None)
curr_dir = None
for line in st.splitlines():
    if line.startswith('$ cd'):
        s, cmd, dir = line.split()
        if dir == "..":
            curr_path.pop()
            curr_dir = curr_dir.parent
        elif dir == "/":
            curr_path = ['/']
            curr_dir = root_dir
        else:
            curr_path.append(dir)
            curr_dir = curr_dir.get_subdir(dir)
    elif line[0] != '$':
        size, name = line.split()
        if size == "dir":
            curr_dir.add_subdir(Directory(name, 0, curr_dir))
        else:
            size = int(size)
            new_file = File(name, size)
            curr_dir.add_subdir(new_file)

# run a dfs from root_dir
total = 0
filesize_map = {}
def total_size_under_100000(node, depth):
    global total
    size = node.get_size()
    filesize_map[node.name] = size
    if size < 100000: 
        total += size
    for child in node.subdirs:
        if isinstance(child, Directory):
            total_size_under_100000(child, depth + 1)

total_size_under_100000(root_dir, 0)
print(total)

# Part 2
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
UNUSED = TOTAL_SPACE - root_dir.get_size()

min_deletable = math.inf
for name, size in filesize_map.items():
    if size < min_deletable and size + UNUSED > NEEDED_SPACE:
        min_deletable = size

print(min_deletable)
