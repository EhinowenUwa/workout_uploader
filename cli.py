# This file communicates with the API endpoint connected to the CLI on the AWS server, which is in turn sending and receiving data from a PostgreSQL database.
from vars import API_CMD
from requests import get

def run_cmd(cmd):
    return get(API_CMD + cmd).text