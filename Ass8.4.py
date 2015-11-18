# 8.4
# Liu Li
# 18 Nov, 2015

'''
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''
# Use the file name romeo.txt as the file name

fname = "romeo.txt"
with open(fname, 'r') as fh:
    lst = list()
    for line in fh:
        temp = line.rstrip("\n").split(" ")
        for s in temp:
            if not (s in lst):
                lst.append(s)
lst.sort()
print lst
