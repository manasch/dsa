import typing
import re
from pathlib import Path

current_directory = Path.cwd().resolve()

def main():
    problems: typing.List = list()
    pattern = re.compile("\[{2}(\d+)\].{3}(.*)\]\((.*)\)")

    for dir in current_directory.iterdir():
        if dir.is_dir():
            for md in dir.iterdir():
                with open(md) as fp:
                    line = fp.readline().strip()
                
                matched = pattern.search(line)
                problems.append([int(matched.group(1)), matched.group(2), md.relative_to(current_directory).as_posix(), dir.name, matched.group(3)])

    problems.sort()
    data: str = ""
    with open(current_directory / "README.md") as fp:
        for _ in range(7):
            data += fp.readline()

    with open(current_directory / "README.md", "w") as fp:
        data += "\n|ID|Name|File|Tag|Link|\n|--|--|--|--|--|\n"
        for problem in problems:
            data += f"|{problem[0]}|{problem[1]}|[{problem[2]}](./{problem[2]})|{problem[3]}|{problem[4]}|\n"
        
        fp.write(data)

if __name__ == "__main__":
    main()
