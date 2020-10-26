import sys
import os
import json

print(os.getenv("GITHUB_REF"))
print("Pull request:", os.getenv("GITHUB_REF").split("/")[2])
print(os.getenv("GITHUB_EVENT_PATH"))

with open(os.getenv("GITHUB_EVENT_PATH")) as fp:
    json_obj = json.load(fp)

print("Pull Request from event.json:", json_obj["number"])

sys.exit(1)
