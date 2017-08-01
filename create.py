import time, nltk, sys
from urllib import urlopen
from bs4 import BeautifulSoup

def printf(format, *args):
    sys.stdout.write(format % args)

def post(zelda):
    html = urlopen(zelda).read()
    param = BeautifulSoup(html, "html.parser")
    out=""
    for tag in param.find_all():
        out+=str(tag)
 #       cari = tag.find("detail_text")
 #       print(cari)
 #   print(out.get_text().encode('utf-8'))
 #   print(out)
    pos1 = out.find("detail_text")
    pos2 = out.find("<!-- POLONG -->")
    for x in range(pos1, pos2):
        printf(out[x])
