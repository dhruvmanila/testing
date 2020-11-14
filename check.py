import sys
import os

env = os.getenv("GITHUB_ENV")
path = os.getenv("GITHUB_PATH")

print(f"{env = }")
print(f"{path = }")

_DELIMITER = "EOF"


def setenv(name: str, value: str) -> None:
    write_value = f"{name}<<{_DELIMITER}{os.linesep}{value}{os.linesep}{_DELIMITER}"
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as file:
        file.write(write_value + os.linesep)


def addpath(path: str) -> None:
    with open(os.environ["GITHUB_PATH"], "a") as path_file:
        path_file.write(str(path) + os.linesep)

        
setenv("HELLO", "WORLD")
setenv("CHANGED", "FALSE")
setenv("CHANGED", "TRUE")

addpath("/path/to/directory")
addpath("/use/bin/local")

with open(env) as f:
    print(f.read(), end=f"{os.linesep}{os.linesep}")

with open(path) as f:
    print(f.read(), end=f"{os.linesep}{os.linesep}")

sys.exit(0)
