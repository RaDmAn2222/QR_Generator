import segno
import pyshorteners

def url_shortener(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url
#function for shortening the url size for a better and compressed QR code


def qr_maker(url):
    qr = segno.make(url, micro=False, error='h')
    qr.save("QR.png", scale=10, dark=(19,58, 27), light=(228, 222, 174))
#function for making the url


url = input("Enter your url: ")

qr_maker(url_shortener(url))

#You can modify the code if you want to make QR code of different things.
#Unless you want to get a compressed url QR code, you need to omit the url_shortener funcition and modify other parts.