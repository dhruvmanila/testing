import sys
import os

print(os.getenv("GITHUB_REF"))
print("Pull request:", os.getenv("GITHUB_REF").split("/")[2])
print(os.getenv("GITHUB_EVENT_PATH"))

print(os.getenv("GITHUB_TOKEN"))
#  print(os.getenv())
#  print(os.getenv())
#  print(os.getenv())
#  print(os.getenv())
#  print(os.getenv())
#  print(os.getenv())



sys.exit(1)
