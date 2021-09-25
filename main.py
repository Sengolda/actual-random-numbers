from hashlib import sha256, sha224, sha384
import requests
import random

method = random.choice([sha384, sha224, sha256])
res = requests.get("https://api.quotable.io/random").json()
hashed = method(res["content"].encode())

random.seed(hashed.hexdigest())

for _ in range(0, 10):
    print(random.randrange(0, 10))
