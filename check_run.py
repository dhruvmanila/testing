import sys
import os
import json
from pprint import pprint

print(os.getenv("GITHUB_API_URL"))

event_path = os.getenv("GITHUB_EVENT_PATH")
print("Event path:", event_path)

with open(event_path) as f:
  event = json.load(f)

pprint(event["number"])
  
sys.exit(0)
