import hashlib

filter = [False] * 16
test_message = "Hello World"

#Returns the hash for the filter
def _generate_hash(hex_digest, filter_size):
    return int(str(hex_digest), 16) % filter_size

#TODO: Allow usage of more than two digests
def _generate_hexdigests(message):
    m = hashlib.sha256()
    m.update(message)
    x = hashlib.md5()
    x.update(message)
    return [m.hexdigest(), x.hexdigest()]

def _generate_hashes(message):
    return [_generate_hash(hd, len(filter)) for hd in _generate_hexdigests(message)]


def addMessage(message):
    truebits = _generate_hashes(message)

    for tb in truebits:
        filter[tb] = True

def checkMessage(message):
    truebits = _generate_hashes(message)
    return all([filter[hash] for hash in truebits])


def test():
    addMessage(test_message)
    print(filter)
    print(checkMessage(test_message))
    print(checkMessage("hello"))

test()
