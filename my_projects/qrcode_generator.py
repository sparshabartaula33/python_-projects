import qrcode as qr
url = input(" Enter the url to make the qr code : ")


img = qr.make(url)

img.save("qr_img.png")
