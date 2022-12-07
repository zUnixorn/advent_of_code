class Dir:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def dir(self, name):
        if name == "..":
            return self.parent

        if name == "/":
            return self.root()

        for existing_dir in self.dirs:
            if existing_dir.name == name:
                return existing_dir

    def root(self):
        if self.name == "/":
            return self

        return self.parent.root()
    
    def add_file(self, size, name):
        self.files.append((size, name))
    
    def add_dir(self, name):
        self.dirs.append(Dir(name, self))
    
    def size(self):
        files_size = sum(file[0] for file in self.files)

        if self.dirs == []:
            return files_size

        return files_size + sum(dir.size() for dir in self.dirs)
    
    def dirs_list(self):
        if self.dirs == []:
            return []

        dirs = self.dirs.copy()

        for dir in self.dirs:
            dirs += dir.dirs_list()

        return dirs

def fs_tree(lines):
    current_dir = Dir("/")
    
    for line in lines:
        line = line.split(' ')
        
        if line[0] == '$':
            if line[1] == "cd":
                current_dir = current_dir.dir(line[2])
            continue
        
        if line[0] == "dir":
            current_dir.add_dir(line[1])
        else:
            current_dir.add_file(int(line[0]), line[1])
    
    return current_dir

def solution(lines):
    return sum(filter(lambda x: x <= 100000, map(lambda x: x.size(), fs_tree(lines).root().dirs_list())))
