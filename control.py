# 1945204 lines total
#count = len(open("control-chr21.fastq").readlines(  ))

lines = []
infile = open("control-chr21.fastq", "r")
lines = infile.readlines()

desired_lines = lines[1::4]

print(len(desired_lines))
outfile = open("control.txt", "w")  #307932 lines in control.txt
for i in desired_lines:
    if len(i) == 26:
        outfile.write(i)

outfile.close()
#print(desired_lines)
