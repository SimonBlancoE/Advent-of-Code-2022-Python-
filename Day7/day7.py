with open('input', 'r') as s:
    data = s.readlines()


def get_dir_sizes() -> dict[str, int]:
    pwd: str = ""
    dirs: dict[str, int] = {"/": 0}

    for line in data:
        line = line.strip()
        if line == "$ ls":
            continue
        elif line == "$ cd /":
            pwd = "/"
        elif line == "$ cd ..":
            pwd = "/".join(pwd.split("/")[:-2]) + "/"
        elif line.startswith("$ cd"):
            pwd += line.split(" ")[-1] + "/"
        elif line.startswith("dir "):
            dirs[pwd + line.split(" ")[-1] + "/"] = 0
        else:
            dirs[pwd] += int(line.split(" ")[0])
    print(dirs)
    return {k: sum([dirs[l] for l in dirs if l.startswith(k)]) for k in dirs}


def part_1() -> int:
    dir_sizes = get_dir_sizes()
    return sum([dir_sizes[d] for d in dir_sizes if dir_sizes[d] <= 100000])


def part_2() -> int:
    dir_sizes = get_dir_sizes()
    space_available = 70000000 - dir_sizes["/"]
    space_needed = 30000000 - space_available
    return min([dir_sizes[d] for d in dir_sizes if dir_sizes[d] >= space_needed])


get_dir_sizes()
print(part_1())
print(part_2())
