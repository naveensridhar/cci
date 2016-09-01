# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
prime = 101 #large prime number

def hash(input):
    h = 0
    pow = len(input)-1
    for i in xrange(len(input)):
        h += ((prime ** pow) * ord(input[i]))
        pow -= 1
    return h

def search(fullstr, substr):
    hash_sub = hash(substr)
    lsub = len(substr)
    lfull = len(fullstr)
    hash_full_init = hash(fullstr[0:lsub])
    if hash_sub == hash_full_init:
        return True
    for i in xrange(0, (lfull - lsub)):
        if hash_full_init == hash_sub:
            return True
        hash_full_init = ((hash_full_init - (ord(fullstr[i]) * (prime**(lsub-1)))) * prime) + ord(fullstr[i + lsub])
    return False
import sys
print search(sys.argv[1], sys.argv[2])
