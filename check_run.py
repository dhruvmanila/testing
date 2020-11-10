import sys
import os
import json

print(os.getenv("GITHUB_REF"))
print("Pull request:", os.getenv("GITHUB_REF").split("/")[2])
print(os.getenv("GITHUB_EVENT_PATH"))

sys.exit(1)
