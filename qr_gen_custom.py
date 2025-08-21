import qrcode

# Data you want to encode
data = "https://shahid.codes"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls size of the QR Code (1 = small, 40 = large)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction
    box_size=10,  # size of each box (pixel per box)
    border=4,  # border thickness (minimum 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr.png")

print("QR Code generated and saved as my_qr.png")
