# 6051 Returns (Reversing, 850pt)

6051\_Returns.exe라는 파일이 하나 주어집니다.

아이다로 분석해보면 중간중간 DPMX 시그니처, HSP3 시그니처를 검사하는 것을 볼 수 있는데 구글에 HSP3 DPMX을 쳐보면 HSP가 Hot Soup Processor의 약자라는 것을 알 수 있습니다.  
이를 통해서 이 바이너리는 HSP라는 언어로 만들어졌다는 것을 파악하고 HSP Decompiler를 검색해보면 [deHSP120.exe](https://github.com/YSRKEN/HSP-Decompiler)라는 프로그램이 나오는데 이걸로 디컴파일 하려고 하면 무언가 에러가 납니다.

![decomerror](https://github.com/5unKn0wn/ctfs/blob/master/2018/codegate_final/6051_Returns/images/decomerror.png)

에러를 번역해보면 DPM 헤더를 검색하다가 중단했는데 내부에 start.ax라는 파일을 추출하는 과정에서 에러가 난듯 싶습니다.  

어차피 바이너리가 실행되면서 DPMX 파일을 복호화 해서 실행을 할 것이기 때문에 분명 바이너리 내부에는 복호화된 메모리가 있을 것이고 우리는 그 복호화된 메모리만 가져오면 됩니다.

바이너리를 분석하면

![startup](file:///Users/5unKn0wn/Desktop/startup.png)

sub\_401D00함수가 실패했을 때 Startup failed라는 메시지를 띄우고 종료시킵니다.  
뭔가 저 안에 중요한 루틴이 있을거 같네요.

![header](file:///Users/5unKn0wn/Desktop/header.png)

내부로 들어가서 보면 sub\_401A00함수가 리턴한 v13변수의 첫 4바이트가 HSP3인지 검사합니다.  
뭔가 HSP 스크립트가 정상적으로 복호화가 된건지 시그니처 체크를 하는 것 같은 냄새가 풍깁니다.

디버깅을 해서 메모리를 추출해 보겠습니다.

![debug](file:///Users/5unKn0wn/Desktop/debug.png)

저 메모리 부분을 가져와서 start.ax로 저장한 후 다시 deHSP120.exe로 디컴파일 해보면 이번엔 정상적으로 디컴파일이 되어 start.hsp를 추출할 수 있습니다.

![extract](file:///Users/5unKn0wn/Desktop/extract.png)

(바이너리에서 직접 복호화 키를 구하여 start.ax 및 리소스를 모두 추출하는 스크립트는 extract_hsp.py에 짜두었습니다.)

이제 추출된 소스코드를 분석할 시간입니다.

```
#uselib "KERNEL32.DLL"

	title "6051 Returns"
	screen 0, 552, 60
	cls 4
	color 255, 255, 255
	font "Arial", 19, 16
	var_0 = ()
	if ( var_0 ) {
		var_1 = "DEBUGGING DETECTED"
	}
	else {
		var_1 = ""
	}
	pos 30, 20
	mes "input : "
	pos 87, 20
	input var_1, 345, 20
	if ( var_0 == 0 ) {
		pos 445, 20
		button "check", *label_00
	}
	stop
*label_00
	randomize 6051
	dim var_2, var_3
	var_4 = 82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125
	var_5 = 227, 88, 27, 251, 109, 62, 47, 28, 51, 100, 65, 206, 242, 129, 245, 198, 199, 238, 36, 137, 22, 141, 90, 135, 183, 247, 42, 207, 65, 242, 147, 151, 159, 126, 241, 197, 178, 121, 168, 33, 5, 197, 43, 67, 118, 77
	var_6 = strlen(var_1)
	var_7 = 0
	var_8 = 0
	var_9 = 1
	repeat var_6
		var_2(cnt) = peek(var_1, cnt)
	loop
	var_10 = 0
*label_01
	exgoto var_10, 1, var_6, *label_04
	var_7 = 0
	var_11 = 0
*label_02
	exgoto var_11, 1, 8, *label_03
	if ( (var_2(var_10) >> var_11 & 1) != (var_2((var_10 + 1) \ var_6) >> 7 - var_11 & 1) ) {
		var_7++
	}
	var_11 += 1
	goto *label_02
*label_03
	var_2(var_10) = var_2(var_10) << (var_7 & 7) & 255 | (var_2(var_10) >> 8 - (var_7 & 7) & 255)
	var_10 += 1
	goto *label_01
*label_04
	var_10 = 0
*label_05
	exgoto var_10, 1, var_6, *label_12
	var_8 = 0
	var_11 = 0
*label_06
	exgoto var_11, 1, var_6, *label_07
	var_8 = var_8 + (var_2(var_11) ^ var_4(-var_2(var_11) - 1 & 255)) - var_2((var_11 + 1) \ var_6) & 255
	var_8 = var_8 >> (var_11 & 7) | (var_8 << 8 - (var_11 & 7) & 255)
	var_8 = var_8 >> (var_2(var_11) & 7) & 255 | (var_8 << 8 - (var_2(var_11) & 7) & 255)
	var_2((var_11 + 1) \ var_6) = var_8
	var_11 += 1
	goto *label_06
*label_07
	var_11 = 0
*label_08
	exgoto var_11, 1, var_6, *label_09
	var_2(var_11) = (var_2(var_11) & 170) >> 1 | ((var_2(var_11) & 85) << 1 & 255)
	var_11 += 1
	goto *label_08
*label_09
	var_11 = 0
*label_10
	exgoto var_11, 1, var_6 - 1, *label_11
	if ( var_2(var_11) != var_2(var_11 + 1) ) {
		var_2(var_11) = var_2(var_11) ^ var_2(var_11 + 1)
		var_2(var_11 + 1) = var_2(var_11) ^ var_2(var_11 + 1)
		var_2(var_11) = var_2(var_11) ^ var_2(var_11 + 1)
	}
	var_11 += 1
	goto *label_10
*label_11
	var_10 += 1
	goto *label_05
*label_12
	var_10 = 0
*label_13
	exgoto var_10, 1, var_6, *label_14
	var_12 = rnd(256)
	var_2(var_10) = var_2(var_10) | var_12 & (256 + ((var_2(var_10) & var_12) * (-1) - 1) & 255)
	var_10 += 1
	goto *label_13
*label_14
	if ( length(var_5) != length(var_2) ) {
		var_9 = 0
	}
	else {
		repeat length(var_5)
			if ( var_2(cnt) != var_5(cnt) ) {
				var_9 = 0
				break
			}
		loop
	}
	if ( var_9 == 1 ) {
		dialog "correct", 4, "correct"
	}
	else {
		dialog "wrong", 1, "wrong"
	}
	end

```

소스의 윗부분(label\_00 이전)은 기본적인 input창 세팅을 하는 부분이고 label\_00부터가 진짜 연산 루틴의 시작입니다.

먼저 랜덤 시드를 6051로 설정하네요.  
HSP에서 쓰이는 랜덤은 c언어에서 rand 함수로 나오는 값과 같습니다(윈도우).  
즉 srand(6051)을 하는것과 같은 행위입니다.  
(참고로 예선과 본선 문제 이름이 6051인 이유는 랜덤 시드를 6051로 설정하기 때문입니다)

다음으로 변수 선언들이 이루어집니다.  
var\_4는 연산할 때 쓰이는 테이블이고 var\_5는 연산이 다 이루어진 뒤 값을 검사할 때 쓰이는 테이블 입니다.  
그리고 var\_1은 input이 들어있는 변수, var\_6은 인풋의 길이, var\_2는 문자열 인풋을 숫자로 변경하여 저장된 배열입니다.

이제 label\_01로 넘어가서 exgoto라는 명령어가 나오는데 exgoto의 매뉴얼은 [여기](http://ohdl.hsproom.me/)서 검색하면 나옵니다.

```
지정 레이블 조건 점프
exgoto var, p1, p2, *label

var : 비교에 사용되는 변수
p1 : 비교 플래그
p2 : 비교 값
*label : 레이블 이름
```

var == p2일 때 label로 점프한다고 합니다.  
즉, 반복문이 goto형태로 변형되었다고 볼 수 있습니다.

이런식으로 추출된 소스를 파이썬으로 포팅하면

```python
inp = [ord(i) for i in raw_input()]
table = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]
cmp_table = [227, 88, 27, 251, 109, 62, 47, 28, 51, 100, 65, 206, 242, 129, 245, 198, 199, 238, 36, 137, 22, 141, 90, 135, 183, 247, 42, 207, 65, 242, 147, 151, 159, 126, 241, 197, 178, 121, 168, 33, 5, 197, 43, 67, 118, 77]
rnd_table = [ 86, 54, 91, 76, 73, 23, 206, 241, 163, 110, 217, 227, 215, 244, 32, 196, 77, 130, 231, 91, 5, 38, 213, 66, 126, 118, 248, 222, 214, 36, 10, 148, 50, 211, 243, 58, 96, 41, 142, 204, 187, 38, 176, 97, 79, 180]
inp_len = len(inp)
is_correct = 1

rol = lambda val, r_bits, max_bits: \
	(val << r_bits%max_bits) & (2**max_bits-1) | \
	((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
	((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

for i in range(inp_len):
	var_7 = 0
	for j in range(8):
		if (inp[i] >> j & 1) != ((inp[(i + 1) % inp_len] >> (7 - j)) & 1):
			var_7 += 1
	# inp[i] = (inp[i] << (var_7 & 7) & 0xff) | (inp[i] >> (8 - (var_7 & 7)) & 0xff)
	inp[i] = rol(inp[i], var_7 & 7, 8)	# same as rol

for i in range(inp_len):
	var_8 = 0
	for j in range(inp_len):
		var_8 = var_8 + (inp[j] ^ table[(~inp[j] & 0xff)]) - inp[(j + 1) % inp_len] & 0xff
		var_8 = (var_8 >> (j & 7)) | (var_8 << 8 - (j & 7) & 0xff)
		# var_8 = (var_8 >> (inp[j] & 7) & 0xff) | (var_8 << 8 - (inp[j] & 7) & 0xff)
		var_8 = ror(var_8, inp[j] & 7, 8)	# same as ror
		inp[(j + 1) % inp_len] = var_8

	for j in range(inp_len):
		inp[j] = ((inp[j] & 170) >> 1) | ((inp[j] & 85) << 1 & 0xff)

	for j in range(inp_len - 1):
		# if inp[j] != inp[j + 1]:
		# 	inp[j] = inp[j] ^ inp[j + 1]
		# 	inp[j + 1] = inp[j] ^ inp[j + 1]
		# 	inp[j] = inp[j] ^ inp[j + 1]
		inp[j], inp[j + 1] = inp[j + 1], inp[j]	# same as swap

for i in range(inp_len):
	# inp[i] = (inp[i] | rnd_table[i]) & (256 + ((inp[i] & rnd_table[i]) * (-1) - 1) & 0xff)
	inp[i] ^= rnd_table[i]	# same as xor

if len(inp) != len(cmp_table):
	is_correct = 0

else:
	for i in range(inp_len):
		if inp[i] != cmp_table[i]:
			is_correct = 0
			break

if is_correct:
	print "correct"

else:
	print "wrong"
```

이렇게 바꿀 수 있습니다.

중간중간 복잡한 연산들은 간단하게 최적화 하면 대부분의 연산은 xor, swap, rol, ror로 나타낼 수 있고 이는 충분히 역연산이 가능합니다.

역연산을 하면

```python
enc = [ 227, 88, 27, 251, 109, 62, 47, 28, 51, 100, 65, 206, 242, 129, 245, 198, 199, 238, 36, 137, 22, 141, 90, 135, 183, 247, 42, 207, 65, 242, 147, 151, 159, 126, 241, 197, 178, 121, 168, 33, 5, 197, 43, 67, 118, 77 ]
rnd_table = [ 86, 54, 91, 76, 73, 23, 206, 241, 163, 110, 217, 227, 215, 244, 32, 196, 77, 130, 231, 91, 5, 38, 213, 66, 126, 118, 248, 222, 214, 36, 10, 148, 50, 211, 243, 58, 96, 41, 142, 204, 187, 38, 176, 97, 79, 180 ]
s = [ 0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
	0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
	0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
	0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
	0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
	0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
	0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
	0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
	0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
	0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
	0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
	0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
	0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
	0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
	0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
	0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D ]

rol = lambda val, r_bits, max_bits: \
	(val << r_bits%max_bits) & (2**max_bits-1) | \
	((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

ror = lambda val, r_bits, max_bits: \
	((val & (2**max_bits-1)) >> r_bits%max_bits) | \
	(val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

enc = [enc[i] ^ rnd_table[i] for i in range(len(enc))]

for i in range(len(enc)):
	for j in range(len(enc) - 1, 0, -1):
		enc[j], enc[j - 1] = enc[j - 1], enc[j]
	for j in range(len(enc)):
		enc[j] = ((enc[j] & 0b10101010) >> 1) | ((enc[j] & 0b01010101) << 1)
	for j in range(len(enc) - 1, -1, -1):
		res = enc[(j + 1) % len(enc)]
		res = rol(res, enc[j] & 7, 8)
		res = (((res << (j & 7)) & 0xff) | ((res >> (8 - (j & 7))) & 0xff))
		res = enc[j] - res + (enc[j] ^ s[~enc[j] & 0xff]) & 0xff
		if j == 0:
			res = (res - enc[j]) & 0xff
		enc[(j + 1) % len(enc)] = res

for i in range(len(enc) - 1, -1, -1):
	l = []
	for j in range(9):
		diff = 0
		tmp = ror(enc[i], j, 8)
		for k in range(8):
			if ((tmp >> k) & 1) != ((enc[(i + 1) % 46] >> (7 - k)) & 1):
				diff += 1
		if (j == diff) and (tmp < 128) and (tmp > 32):
			l.append(tmp)
	if len(l) == 1:
		enc[i] = l[0]
	else:
		print "What is correct?"
		for _ in range(len(l)):
			print "%d." % (_ + 1),
			print chr(l[_]) + ''.join(chr(c) for c in enc[i + 1:])
		c = input(">> ")
		enc[i] = l[c - 1]

print ''.join(chr(i) for i in enc)
```

이렇게 나타낼 수 있고 마지막 연산 부분에서 2~3가지 정도의 중복 답이 나올 수 있기에 사용자에게 어떤 값으로 연산할지를 물어보는 부분이 있습니다.

![flag](file:///Users/5unKn0wn/Desktop/flag.png)

> FLAG{C0ngr4tz,\_It\_1s\_s0\_D3l1c10us\_H0t\_S0uP\_:)}
