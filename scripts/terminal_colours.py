#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
    Colorize String Module
    License: you can do what ever you want with this file a long as you put
             NinjaGeek in you credits, if not this file will self-destruct and
             destroy your system... for real!!!
    NOTE: script's importing this module must have encoding declared as utf-8
    EX: # -*- coding:utf-8 -*-
'''


CLR_THIN = 0
CLR_THIC = 1
CLR_THGR = 2  # thin gray
CLR_UNLI = 4  # underline
CLR_BGWH = 7  # white background
CLR_TRAN = 8  # transparent
CLR_STRT = 9  # strike-trough
CLR_GRAY = 30
CLR_RED  = 31
CLR_GRN  = 32 # green
CLR_YLW  = 33 # yellow
CLR_BLUE = 34
CLR_MGNT = 35 # magenta
CLR_CYAN = 36
CLR_WHT  = 37 # white
CLR_BGBA = 40 # black background
CLR_BGRD = 41 # red background
CLR_BGGR = 42 # green background
CLR_BGBR = 43 # light-brown/pastel-yellow background (idk) :P
CLR_BGBL = 44 # blue background
CLR_BGMG = 45 # magneta background
CLR_BGCY = 46 # cyan background
CLR_BGLG = 47 # gray background
CLR_BGDG = 100# dark-gray background

def colorize(txt, color):
    colored = '\033[1;%dm%s\033[1;m' % (color, txt)
    return colored

c=colorize

print c('Thin White', CLR_THIN)
print c('Thick White', CLR_THIC)
print c('Thin Gray', CLR_THGR)
print c('Underline', CLR_UNLI)
print c('White Background', CLR_BGWH)
print c('Transparent Text', CLR_TRAN), '<- (Transparent Text)'
print c('Strike-trough', CLR_STRT)
print c('Gray Text', CLR_GRAY)
print c('Red Text', CLR_RED)
print c('Green Text', CLR_GRN)
print c('Yellow Text', CLR_YLW)
print c('Blue Text', CLR_BLUE)
print c('Magenta Text', CLR_MGNT)
print c('Cyan Text', CLR_CYAN)
print c('Light-gray Text', CLR_WHT)
print c('Black Background', CLR_BGBA)
print c('Red Background', CLR_BGRD)
print c('Green Background', CLR_BGGR)
print c('Brown/Yellow-ish background', CLR_BGBR)
print c('Blue Background', CLR_BGBL)
print c('Magenta Background', CLR_BGMG)
print c('Cyan Background', CLR_BGCY)
print c('Light-gray Background', CLR_BGLG)
print c('Dark-gray Background', CLR_BGDG)
