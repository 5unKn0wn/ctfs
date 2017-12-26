from PIL import *
import Image
import os

for i in range(777):
    data = []
    start, middle, end = None, None, None
    with open("%d/1" % (i + 1), "rb") as f:
        data.append(f.read())
    with open("%d/2" % (i + 1), "rb") as f:
        data.append(f.read())
    with open("%d/3" % (i + 1), "rb") as f:
        data.append(f.read())

    for j in data:
        if j.startswith("\x89\x50\x4E\x47"):
            start = j
        elif j[-8:] == "\x49\x45\x4E\x44\xAE\x42\x60\x82":
            end = j
        else:
            middle = j

    with open("%d/ok.png" % (i + 1), "wb") as f:
        f.write(start + middle + end)

new = Image.new("RGB", (777 * 2, 777))
for i in range(777):
    im = Image.open("%d/ok.png" % (i + 1))
    for j in range(2):
        for k in range(777):
            new.putpixel((i * 2 + j, k), im.getpixel((j, k)))

new.save("flag.png")
