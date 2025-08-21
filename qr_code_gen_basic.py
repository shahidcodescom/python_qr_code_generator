import qrcode  

data = "https://shahid.codes"  
img = qrcode.make(data)  
img.save("my_qr.png")  
