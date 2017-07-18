import random
import string

rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])

print rand_str(100)
