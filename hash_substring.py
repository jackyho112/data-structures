# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(string, prime, multiplier):
    hash_index = 0
    for c in reversed(string):
        hash_index = (hash_index * multiplier + ord(c)) % prime
    return hash_index

def doHashes(text, pattern_length, prime, multiplier):
    hashes = [None] * (len(text) - pattern_length + 1)
    string = text[len(text) - pattern_length:]
    hashes[len(text) - pattern_length] = polyhash(string, prime, multiplier)
    index = 1
    for i in range(pattern_length):
        index = (index * multiplier) % prime
    for i in range(len(text) - pattern_length - 1, -1, -1):
        hashes[i] = (multiplier * hashes[i + 1] + ord(text[i]) - index * ord(text[i + pattern_length])) % prime

    return hashes

def get_occurrences(pattern, text):
    result = []
    prime = 1480978657
    multiplier = 193
    p_hash = polyhash(pattern, prime, multiplier)
    main_hash = doHashes(text, len(pattern), prime, multiplier)

    for i in range(len(text) - len(pattern) + 1):
        if (p_hash == main_hash[i]) and (text[i:i + len(pattern)] == pattern):
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
