#Import segno library
from segno import helpers

def get_full_qrcode(n, ln, e, u, p):
    """
    It will return a .svg QR Code file
    n = First Name
    l = Last Name
    e = E-mail
    u = URL. Do not use http:// or https://. Only your domain name, example: mydomain.com
    p = phone
    """
    qr = helpers.make_mecard(name=ln+","+n, email=e, url=u, phone=p)
    qr.save(str(n)+"_"+str(ln)+".png", scale=10, dark="darkblue")

n = "Alberto"
ln = "Castillo"
e = "albertocastilloa@me.com"
u = "github.com/albertocastilloa"
p = "5512345678"

#Call the function
get_full_qrcode(n, ln, e, u, p)
