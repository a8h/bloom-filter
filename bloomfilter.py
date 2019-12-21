import hashlib

filter = [False] * 16
test_message = "Hello World"

def hexdigestToBits(hex_digest, filter_size):
    return int(str(hex_digest), 16) % filter_size

def generate_hexdigests(test_message):
    m = hashlib.sha256()
    m.update(test_message)
    x = hashlib.md5()
    x.update(test_message)
    return [m.hexdigest(), x.hexdigest()]
    

truebits = [hexdigestToBits(hd, len(filter)) for hd in generate_hexdigests(test_message)]

for tb in truebits:
    filter[tb] = True

print(filter)

