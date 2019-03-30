import os
so_20000 = []

game1 = open("20000_returnz_ver/game1.txt", "rb").read().rstrip().split('\n')
lgame1 = []
for i in game1:
	so_20000.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
	lgame1.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
lgame2 = []
game2 = open("20000_returnz_ver/game2.txt", "rb").read().rstrip().split('\n')
for i in game2:
	so_20000.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
	lgame2.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
lgame3 = []
game3 = open("20000_returnz_ver/game3.txt", "rb").read().rstrip().split('\n')
for i in game3:
	so_20000.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
	lgame3.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
allgame = open("20000_returnz_ver/allgame.txt", "rb").read().rstrip().split('\n')
allgame_list = []
for i in allgame:
	so_20000.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))
	allgame_list.append(int(i.split("Binary file ./20000_so/lib_")[1].split(".so")[0]))

for i in allgame_list:
	dat = open("20000_returnz_ver/20000_so/lib_%d.so" % i, "rb").read()
	if dat.find("\x85\xC0\x7E\x08\x8B\x45\xF4\x83\xF8\x04\x7E\x0A") == -1:
		print i