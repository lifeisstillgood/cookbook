#!/usr/local/bin/python
#! -*- coding:utf-8 -*-

"""
pbrian

Simple script to run preset sox then lame conversion
over a set of ball calls.
Also use for "shouts".
Do on a per directory basis.
Create beginnings of a map for this

raw > normalise > mp3

companding


Notes

Dynamic range compression is a means of bumping up the gain on
all sounds in a certain range (or rather within an attack profile like that of human voice)
so the voice is brought out and made louder while the noise is left behind.

sox foo.wav asz-car2.wav compand 0.3,1 6:-70,-60,-20 -8 -90 0.2

this is known as companding.

Useful for making cleaner 


"""

import subprocess
import os
import shutil
import re

def runcmd(cmd):
    '''just do one '''
    try:
        val = subprocess.check_call(cmd)
    except subprocess.CalledProcessError, e:
        raise e

def parse_filename(f):
    '''best guess at ball number and description '''
    r = re.compile("(.*?)(\d+)(.*)") # description, ball, take    
    m = r.match(f)
    if not m:
        return [f, "0",""] # no regex match
    return m.groups()

def main():
    
    #get directory contents
    thisdir = "shouts"
    normdir = os.path.join(thisdir, "compand")
    mp3dir = os.path.join(thisdir, "mp3_compand")
    if os.path.isdir(normdir) == False:
        os.mkdir(normdir)
    if os.path.isdir(mp3dir) == False:
        os.mkdir(mp3dir)
   
    files = [f for f in os.listdir(thisdir) if os.path.splitext(f)[1].lower() == '.wav']

    fo = open("mapshouts.txt", "a")
    for f in files:
        desc, ball, junk = parse_filename(f)
        fo.write("%s,%s\n" % (desc, ball))

        infile = os.path.join(thisdir, f)
        normfile = os.path.join(normdir, f)
        mp3file = os.path.join(mp3dir, f.lower().replace(".wav", ".mp3"))

#        cmd = ["sox", "--norm", infile, "-b", "16", normfile, "rate", "44100", "dither", "-s"]
#        print f, "normalising...",
        print f, "companding...",
        cmd = ["sox", infile, normfile, "compand", "0.3,1", "6:-70,-60,-20", "-8", "-90", "0.2"]

        runcmd(cmd)
        cmd2 = ["lame", "--quiet", "-a", "-m", "m", "-b", "32", "-h", "-s", "22.05",
                "--resample", "22.05", normfile, mp3file]    
        print "mp3...", 
        runcmd(cmd2) 
        print "done"
    fo.close()

if __name__ == '__main__':
    main()
