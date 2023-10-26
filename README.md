<h1>QR Code Generator</h1>

This is a Python program of generating a QR code of your own .
In the Output you can get image of qr code as well as the link assigned to the qr code

- For creating a Qr code i've used the qrcode library in the python 
- For getting the link of the qrcode from the image generated i've used the decode class in the pyzbar library along Image class in pillow library


<h4>qrcode</h4>
A Quick Response Code (QR) code is a two-dimensional barcode that can store data, such as text or a web link. They are widely used for various applications like mobile payments, advertising, and product labeling.
Python has a library called qrcode that can be used to generate QR codes. To create a QR code, you need to create a QRCode object and then call the make() function. The make() function takes the data that you want to encode as an argument.

<h4>pyzbar</h4>
The pyzbar library enables your Python scripts to read one-dimensional barcodes and QR codes. It is really simple and easy to use, as you can read codes with a simple “decode” command from an image, getting also info regarding data and position of your QR/bar-codes from the image.

<h4>pillow</h4>
Pillow is a Python Imaging Library (PIL) that adds support for opening, manipulating, and saving images. It is the successor to PIL, which was discontinued in 2011. Pillow supports many image file formats, including PNG, JPEG, TIFF, and BMP.
