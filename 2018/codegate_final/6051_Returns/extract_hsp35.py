# extract packed files for HSP3.5
import struct
import sys

u16 = lambda x : struct.unpack("<H", x)[0]
u32 = lambda x : struct.unpack("<L", x)[0]

class PackedFile:
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
		self.null = u32(f.read(4))
		self.packed_files = [PackedFile(f) for i in range(self.file_count)]
		for i in range(self.file_count):
			self.packed_files[i].data = f.read(self.packed_files[i].file_size)
		self.binary_key = self.get_binary_key(f)

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

	def get_binary_key(self, f):
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
		f.seek(pos)

		return key

	def all_extract(self):
		for ins in self.packed_files:
			self.extract(ins)

	def extract(self, ins):
		decode_key = self.get_file_key(self.binary_key, ins.key, ins.file_size)
		data = self.data_decode(decode_key, ins.data)
		with open(ins.filename, "wb") as f:
			f.write(data)
		print "%s extracted" % (ins.filename)

	def get_file_key(self, binary_key, file_key, file_size):
		key1 = (file_size ^ ((binary_key & 0xff) * ((binary_key >> 16) & 0xff)) / 3) & 0xff
		key2 = (file_size ^ (((binary_key >> 24) & 0xff) * ((binary_key >> 8) & 0xff)) / 5 ^ 0xaa) & 0xff
		key3 = ((file_key & 0xff) + 0x5a) ^ ((file_key >> 16) & 0xff)
		key4 = (((file_key >> 8) & 0xff) + 0xa5) ^ ((file_key >> 24) & 0xff)

		return [(key1 + key3) & 0xff, (key2 + key4) & 0xff]

	def data_decode(self, decode_key, data):
		decoded = ''
		res = 0

		for c in data:
			res = (res + ((ord(c) ^ decode_key[0]) - decode_key[1])) & 0xff
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