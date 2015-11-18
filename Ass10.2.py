# 10.2
# Liu Li
# 18 Nov, 2015

'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
import re
# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
fname = "mbox-short.txt"
with open(fname, 'r') as fh:
    dir = {}
    for line in fh:
        if re.search("From ", line):
            h = re.findall('[\s]([\d]{2})\:', line)[0]
            dir[h] = dir.get(h, 0) + 1
key = sorted(list(dir.keys()))
for k in key:
    print k,dir[k]

#######################################################
# Desired Output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
