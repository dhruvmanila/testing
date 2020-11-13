import sys
import os
import json
from pprint import pprint

print(os.getenv("GITHUB_REF"))
print(os.getenv("GITHUB_EVENT_PATH"))

env = os.getenv("GITHUB_ENV")
path = os.getenv("GITHUB_PATH")

print(f"{env = }")
print(f"{path = }")

with open(env) as f:
  for line in f:
    print(line)

with open(path) as f:
  for line in f:
    print(line)

sys.exit(0)
