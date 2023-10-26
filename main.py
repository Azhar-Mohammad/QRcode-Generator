import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

codeBox = qrcode.make("https://www.geeksforgeeks.org/")

codeBox.save("QRCode.png", scale=8)

link = decode(Image.open("QRCode.png"))
print(link[0].data.decode("ascii"))

