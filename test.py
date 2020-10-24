import sys
import os
import json
from pprint import pprint

print(os.getenv("GITHUB_REF"))
print("Pull request:", os.getenv("GITHUB_REF").split("/")[2])
print(os.getenv("GITHUB_EVENT_PATH"))

with open(os.getenv("GITHUB_EVENT_PATH")) as fp:
    json_obj = json.load(fp)

#  pprint(json_obj, indent=4)


print("Pull Request from event.json:", json_obj["number"])

print("Secret github token:", os.getenv("GITHUB_TOKEN"))

sys.exit(1)
