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
    """Creates or updates an environment variable for any actions running next in a
    job."""
    file_path = os.environ.get("GITHUB_ENV", "")
    cmd_value = f"{name}<<{_DELIMITER}{os.linesep}{value}{os.linesep}{_DELIMITER}"
    print(cmd_value)
    with open(file_path, "a") as file_handle:
        file_handle.write(cmd_value + os.linesep)


setenv("HELLO", "WORLD")
setenv("FROM", "CHANGED")
sys.exit(0)
