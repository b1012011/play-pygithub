#!/usr/bin/env python
# -*- coding: utf-8 -*-
#mecab.py

import MeCab
print "choose output menu (mecabrc,ochasen,owakati,oyomi)"
menu = raw_input("menu>")
text = raw_input("text>")

if menu == "mecabrc":
    m = MeCab.Tagger("mecabrc")
elif menu == "ochasen":
    m = MeCab.Tagger("-Ochasen")
elif menu == "owakati":
    m = MeCab.Tagger("-Owakati")
elif menu == "oyomi":
    m = MeCab.Tagger("-Oyomi")   

try:
    node = m.parseToNode(text)
    while node:    
        print node.feature
        node = node.next
#    f = open('mecabtxt/mtxt','a')
#    f.write(mtxt)
#    f.close()
except NameError:
    print menu,"menu is not exist"