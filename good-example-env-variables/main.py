import os
from dotenv import load_dotenv

# determining the directory path that includes "main.py"
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# if .env file exists, loads and possibly updates env-variables
load_dotenv(os.path.join(PROJECT_DIRECTORY, ".env"))

API_USER_ID = os.getenv("API_USER_ID")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# throws error if variables haven't been set
assert None not in [API_USER_ID, API_SECRET_KEY,], (
    "It is necessary to set both API_USER_ID and API_SECRET_KEY "
    + "either via a '.env' file or the environment variables"
)

# using the variables the same way as before
print(
    f'Connecting to API using USER_ID "{API_USER_ID}" '
    + f'and SECRET_KEY "{API_SECRET_KEY}".'
)
