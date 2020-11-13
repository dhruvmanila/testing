import sys
import os
import json

print(os.getenv("GITHUB_REF"))
print(os.getenv("GITHUB_EVENT_PATH"))

env = os.getenv("GITHUB_ENV")
path = os.getenv("GITHUB_PATH")

print(f"{env = }")
print(f"{path = }")

_DELIMITER = "EOF"


def setenv(name: str, value: str) -> None:
    with open(os.environ["GITHUB_ENV"], "a") as env_file:
        env_file.write(f"{name}={value}" + os.linesep)


def addpath(path: str) -> None:
    with open(os.environ["GITHUB_PATH"], "a") as path_file:
        path_file.write(path + os.linesep)


setenv("HELLO", "WORLD")
setenv("FROM", "CHANGED")

addpath("/path/to/directory")
addpath("/use/bin/local")

with open(env) as f:
    print(f.read())

with open(path) as f:
    print(f.read())

sys.exit(0)
