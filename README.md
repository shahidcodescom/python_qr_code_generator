# python_qr_code_generator
QR Code Generator code using Python


qrcode.QRCode → Creates a customizable QR code object.

version → Controls the dimensions (1 → 21x21 boxes, 2 → 25x25, etc).

error_correction → Lets QR codes still work even if damaged:

L (7% recovery), M (15%), Q (25%), H (30%).

box_size → How many pixels each “box” of the QR code will be.

border → Empty space around the QR code (minimum is 4).

qr.add_data() → The actual text, link, or data you want to encode.

make(fit=True) → Fits the QR code size automatically to your data.

make_image() → Converts the QR object into an image (you can customize colors).

img.save() → Saves the final QR code as a PNG file.
