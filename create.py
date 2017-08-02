import time, nltk, sys
from urllib import urlopen
from bs4 import BeautifulSoup

def printf(format, *args):
    sys.stdout.write(format % args)

def submissionLinkParsing(zelda):
    q = zelda
    # here goes catagorizing the link

def commentBuilder(zelda):
    html = urlopen(zelda).read()
    param = BeautifulSoup(html, "html.parser")
    out=""
    for tag in param.find_all():
        out+=str(tag)
    pos1 = out.find("detail_text")
    pos2 = out.find("<!-- POLONG -->")
    for x in range(pos1, pos2):
        printf(out[x])
    return out
