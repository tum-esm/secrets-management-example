import json
import os

# determining the directory path that includes "main.py"
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# loading the secret variables from a file that is not
# included in the Git-repository
with open(os.path.join(PROJECT_DIRECTORY, "config.json"), "r") as f:
    config = json.load(f)
    API_USER_ID = config["API_USER_ID"]
    API_SECRET_KEY = config["API_SECRET_KEY"]

# using the variables the same way as before
print(
    f'Connecting to API using USER_ID "{API_USER_ID}" '
    + f'and SECRET_KEY "{API_SECRET_KEY}".'
)
