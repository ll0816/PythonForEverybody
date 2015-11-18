# Ass6.5
# created by: Liu Li

'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475";

# 1. extract the float number by trickily locate the '.' then extrac the whole float number.'

pos = text.find(".")
num = text[pos-1:]
print float(num)

# 2. extract the float number by using Regex match the pattern of float number.
import re
num = re.findall("\d*\.\d+", text)[0]
print float(num)

