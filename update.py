import json
import pathlib
import typing
import re
from collections import defaultdict
from pathlib import Path

current_directory = Path.cwd().resolve()

class Parser:
    def __init__(self):
        self.ignored_folders = set()
        self.table_header = "|ID|Name|File|Tag|Link|\n|--|--|--|--|--|"
        self.readme_unchanged_no_lines = 7

        with open("ignore_folders") as f:
            for ignored_folder in f:
                self.ignored_folders.add(ignored_folder.strip())

    def problems_in_folder(self, directory: pathlib.PurePath) -> list:
        problems: dict = defaultdict(list)
        pattern: typing.Pattern = re.compile("\[{2}(\d+)\].{3}(.*)\]\((.*)\)")

        for item in directory.iterdir():
            if item.is_dir():
                for md in item.iterdir():
                    with open(md) as fp:
                        line = fp.readline().strip()
                    
                    matched = pattern.search(line)
                    problems[f"{item.name}"].append([
                        int(matched.group(1)),
                        matched.group(2),
                        md.relative_to(directory).as_posix(),
                        item.name,
                        matched.group(3)
                    ])
        
        return problems
    
    def generate_md(self, site_directory: pathlib.PurePath):
        readme = (site_directory / "README.md").resolve()
        readme_file = []
        push = readme_file.append

        problems = self.problems_in_folder(site_directory)

        with open(readme) as fp:
            for _ in range(self.readme_unchanged_no_lines):
                push(fp.readline().strip())
            push("")
        
        for tag in problems:
            push(f"## {tag.capitalize()}")
            push("")
            push(self.table_header)
            for problem in sorted(problems[tag]):
                push(f"|{problem[0]}|{problem[1]}|[{problem[2]}](./{problem[2]})|{problem[3]}|{problem[4]}|")
            push("")
        
        with open(readme, "w") as fp:
            fp.write("\n".join(readme_file))
    
    def parse(self):
        for directory in current_directory.iterdir():
            if directory.is_dir() and directory.name not in self.ignored_folders:
                self.generate_md(directory.resolve())

def main():
    parser = Parser()
    parser.parse()

if __name__ == "__main__":
    main()
