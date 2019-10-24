import sha3

target = "C81477CEFC17B7241647696EDD01341E156B6C3073ACF9BD4413168AE5F04A062D7F75C508".decode("hex")

def dfs(flag, i):
    if flag.startswith("flag{"):
        return flag
    l = []
    for c in range(32, 127):
        cur = chr(c) + flag
        if sha3.sha3_512(cur).digest()[0] == target[i]:
            l.append(chr(c))
    if len(l) == 1:
        return dfs(l[0] + flag, i + 1)
    elif len(l) == 0:
        return None
    else:
        for c in l:
            res = dfs(c + flag, i + 1)
            if res != None:
                return res
    return None

print dfs('', 0)