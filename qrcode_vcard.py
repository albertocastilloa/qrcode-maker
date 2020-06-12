from segno import helpers

def get_full_qrcode(n, ln, e, u, p):
    qr = helpers.make_mecard(name=ln+","+n, email=e, url=u, phone=p)
    qr.save(str(n)+"_"+str(ln)+".png", scale=10, dark="darkblue")

n = "Alberto"
ln = "Castillo"
e = "albertocastilloa@me.com"
u = "github.com/albertocastilloa"
p = "5512345678"

get_full_qrcode(n, ln, e, u, p)