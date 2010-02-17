#!/usr/local/bin/python
#! -*- coding:utf-8 -*-

"""
Supporting svn management 

Mapping tickets to changesets
Mapping changesets that need to be uploaded 

help with merging up and down
bisecting (sortof) to find missing diffs upon failure

initial - Ham
BRANCH
A - changes filling to cheese - CI
b - changes filling to spam - CI
A - changes filling to cheese, adds in chips.txt - CI
B - changes chips to thin chips - CI 
A - cheese and tomato and fat chips - CI
merge - want cheese tomato and fat chips -

chips file will work ok.
cheese will fail.
Need to have way to see the needed diffs...


THings to do

- python based execution to control better - esp merging
- have some good examples - b commits to brach as well, see blame working etc etc



"""
