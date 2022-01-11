import qrcode
link=input("enter any link for qrcode\n")
img=qrcode.make(link)
img.show("qrcode.png")