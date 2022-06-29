import qrcode

website = 'https://prashantmalla.com.np/'

img = qrcode.make(website)
img.save('qr.png')