import sys
import os
import json
from pprint import pprint

print(os.getenv("GITHUB_REF"))
print("Pull request:", os.getenv("GITHUB_REF").split("/")[2])
print(os.getenv("GITHUB_EVENT_PATH"))

json_obj = json.load(os.getenv("GITHUB_EVENT_PATH"))

pprint(json_obj, indent=4)


print("Pull Request from event.json:", json_obj["number"])

print("Secret github token:", os.getenv("secrets.GITHUB_TOKEN"))

sys.exit(1)
