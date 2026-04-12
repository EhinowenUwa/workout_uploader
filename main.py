import requests

def _read_env(env):
    body = {}
    env = env.split("\n")
    for var in env:
        key, value = var.split("=")
        body[key] = value
    return body

with open(".env", "r") as f:
    env = _read_env(f.read())

API_ENDPOINT = env["API_ENDPOINT"]
API_CMD = API_ENDPOINT + "?cmd="
print(API_CMD)
