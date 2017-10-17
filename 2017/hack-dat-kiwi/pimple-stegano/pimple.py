from PIL import Image

img_name = '../the-troll.png'
img = Image.open(img_name)
pixels = img.getdata()

bits = []
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pix = pixels[(y * 462) + x]
        if pix <= 97:
            bits.append('1' if pix & 0x1 else '0')
bits = ''.join(bits)

decoded = ''.join([chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)])
print decoded
