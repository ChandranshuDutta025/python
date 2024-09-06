import qrcode

img = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
img.add_data("Hello World")
img.make(fit=True)

qr_image = img.make_image(fill='white',back_color="blue")
qr_image.save("qrcode.png")