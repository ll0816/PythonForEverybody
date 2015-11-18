# Ass7.2
# created by: Liu Li
'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
import re
fname = "mbox-short.txt"

with open(fname, 'r') as fh:
    accumulator = 0
    count = 0
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            str_num = re.findall('\d+\.\d*', line)[0]
            accumulator += float(str_num)
            count += 1

print "Desired Output:\nAverage spam confidence: 0.750718518519\n"
print "My Output: "
print "Average spam confidence: " + str(accumulator/count)
