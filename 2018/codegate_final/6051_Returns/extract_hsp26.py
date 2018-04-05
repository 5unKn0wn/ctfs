# extract packed files for HSP2.6
import struct
import sys

u16 = lambda x : struct.unpack("<H", x)[0]
u32 = lambda x : struct.unpack("<L", x)[0]

class FileEntry:
	def __init__(self, f):
		self.filename = f.read(16).rstrip('\x00')
		self.ffffffff = u32(f.read(4))
		self.key = u32(f.read(4))
		self.offset = u32(f.read(4))
		self.file_size = u32(f.read(4))
		self.data = ""

class DPM:
	def __init__(self, f):
		self.data = f.read()
		self.exe_size = self.get_exe_size(self.data)
		self.dpm_data = self.data[self.exe_size:]
		f.seek(self.exe_size)
		self.magic = f.read(4)
		assert self.magic == "DPMX"
		self.data_offset = u32(f.read(4))
		self.file_count = u32(f.read(4))
		self.magic2 = u32(f.read(4))
		self.entries = [FileEntry(f) for i in range(self.file_count)]
		for i in range(self.file_count):
			self.entries[i].data = f.read(self.entries[i].file_size)
		self.secret_key = self.get_secret_key(f)

	def get_exe_size(self, data):
		pos = f.tell()
		f.seek(0x3c)
		e_lfanew = u32(f.read(4))
		f.seek(e_lfanew)
		assert f.read(4) == "PE\x00\x00"
		f.seek(f.tell() + 2)
		NumberOfSections = u16(f.read(2))
		f.seek(f.tell() + 12)
		SizeOfOptionalHeader = u16(f.read(2))
		f.seek(f.tell() + 2 + SizeOfOptionalHeader + ((NumberOfSections - 1) * 40) + 16)
		SizeOfRawData = u32(f.read(4))
		PointerToRawData = u32(f.read(4))
		exe_size = SizeOfRawData + PointerToRawData
		f.seek(pos)

		return exe_size

	def get_secret_key(self, f):
		pos = f.tell()
		f.seek(0, 2)
		size = f.tell()
		f.seek(0)
		for i in range(size):
			f.seek(i)
			data = f.read(13)
			if data[0] == 'x' and data[3] == 'y' and data[6] == 'd' and data[9] == 's' and data[12] == 'k':
				break
		if f.tell() == size:
			key = 0x00000000
		else:
			key = u32(f.read(4))
		print "Secret key : " + hex(key)
		f.seek(pos)

		return key

	def all_extract(self):
		for ins in self.entries:
			self.extract(ins)

	def extract(self, ins):
		keys = self.get_filekey(self.secret_key, ins.key, ins.file_size)
		data = self.data_decode(keys, ins.data)
		with open(ins.filename, "wb") as f:
			f.write(data)
		print "file : %s\tsize : %d" % (ins.filename, ins.file_size)

	def get_filekey(self, secret_key, filekey, file_size):
		x1 = ((secret_key & 0xff) * ((secret_key >> 16) & 0xff) * 0x55555556) >> 32
		s1 = (((x1 >> 31) + x1) ^ file_size) & 0xff

		x2 = ((secret_key >> 8) & 0xff) * ((secret_key >> 24) & 0xff) * 0x66666667 >> 33
		s2 = (((x2 >> 31) + x2) ^ file_size ^ 0xAA) & 0xff

		key1 = ((((filekey & 0xff) + 0x55) ^ ((filekey >> 16) & 0xff)) + s1) & 0xff
		key2 = (((((filekey >> 8) & 0xff) + 0xAA) ^ ((filekey >> 24) & 0xff)) + s2) & 0xff

		return [key1, key2]

	def data_decode(self, keys, data):
		decoded = ''
		res = 0

		for c in data:
			res = (res + ((ord(c) - keys[1]) ^ keys[0])) & 0xff
			decoded += chr(res)

		return decoded


if len(sys.argv) < 2:
	print "python %s [filename]" % sys.argv[0]
	sys.exit()

filename = sys.argv[1]
f = open(filename, "rb")
dpm = DPM(f)
f.close()
dpm.all_extract()
