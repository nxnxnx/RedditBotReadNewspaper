import time, nltk, sys
from urllib import urlopen
from bs4 import BeautifulSoup
import re

def printf(format, *args):
    sys.stdout.write(format % args)

def submissionLinkParsing(zelda):
    regex = ur"\.(.+?)\.+?"
    link = re.findall(regex, zelda)
    if (link==[]):
        regex = ur"(.+?)\.+?"
        link = re.findall(regex,zelda)
    return link[0]
    # here goes catagorizing the link

def commentBuilder(zelda):
    html = urlopen(zelda).read()
    param = BeautifulSoup(html, "html.parser")
    out=""

    for tag in param.find_all():
        out+=str(tag)

    comment=""

    if (submissionLinkParsing(zelda)=='kompas'):
        comment+=kompasCommentBuilder(out)
    elif (submissionLinkParsing(zelda)=='detik'):
        comment+=detikCommentBuilder(out)

    return comment

def kompasCommentBuilder(content):
    #content is a string variable
    #here goes kompasCommentBuilder
    #content is always under  <div class="read__content"> tag

def tirtoCommentBuilder(content):
    #content is a string variable
    #here goes tirtoCommentBuilder
    #content is always under <div class="content-text-editor"> tag 

def detikCommentBuilder(content):
    #content is a string variable
    #here goes detikCommentBuilder
    #content is always under  <div class="detail_text" id="detikdetailtext"> tag
