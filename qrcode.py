import os # give acess to operating system
import qrcode
img = qrcode.make("https://youtu.be/zWh3CShX_do")
img.save("qr.png", "PNG")
os.system(" open qr.png")