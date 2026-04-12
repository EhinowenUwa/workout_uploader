RESET = "\x1b[0;0m"
BLACK = "\x1b[0;30m"
RED = "\x1b[0;31m"
GREEN = "\x1b[0;32m"
YELLOW = "\x1b[0;33m"
BLUE = "\x1b[0;34m"
PURPLE = "\x1b[0;35m"
CYAN = "\x1b[0;36m"
WHITE = "\x1b[0;37m"

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

if __name__ == "__main__":
    print(API_CMD)

