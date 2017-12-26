import angr

p = angr.Project("./unlock_me")
find=(0x00400FC8,)
avoid=(0x400FEC, 0x401010)

init = p.factory.blank_state()
pg = p.factory.path_group(init)
ex = pg.explore(find=find,avoid=avoid)
print ex

print pg.found[0].state.posix.dumps(0)
print pg.found[0].state.posix.dumps(1) 
