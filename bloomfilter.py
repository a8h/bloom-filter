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

def view_filter():
    return ['X' if i else ' ' for i in filter]

def test():
    print("Filter before adding any messages: {}".format(view_filter()))
    addMessage(test_message)
    print("Filter after adding message '{}' : {}".format(test_message, view_filter()))
    print(checkMessage(test_message))
    print(checkMessage("hello"))

test()
