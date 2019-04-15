import random

#adding 0 to negative seq

lines = []
infile = open("control-chr21.fastq", "r")
lines = infile.readlines()

desired_lines = lines[1: :4]

print(len(desired_lines)) #307932


print(len(desired_lines))
outfile = open("control.txt", "w")  #486301 lines in seq.txt
for i in desired_lines:
    if len(i) == 26:
        outfile.write("0")
        outfile.write(i)

outfile.close()


#adding 1 to positive seq

infile = open("nrsf-chr21.fastq", "r")
lines = infile.readlines()

desired_lines = lines[1::4]

print(len(desired_lines))
outfile = open("training.txt", "w")  #486301 lines in seq.txt
for i in desired_lines:
    if len(i) == 26:
        outfile.write("1")
        outfile.write(i)

outfile.close()




# opening control file (negative seq)
infile = open("control.txt", "r") # 307932 lines in seq_control.
lines_control = infile.readlines()
c_lines = lines_control[:]
print(len(c_lines))

# opening seq file (positive seq)
infile2 = open("training.txt", "r") #486301 lines in seq_pos.txt
lines_seq = infile2.readlines()
s_lines = lines_seq[:]
print(len(s_lines))

# print total lines of both files above
print("total: ", len(c_lines) + len(s_lines))

# creating new file containg sequences from  both files above

outfile = open("training_training_labels.txt", "w")  #794233 lines in seq_control_labels.txt
for i in lines_control:
    outfile.write(i)

for j in lines_seq:
    outfile.write(j)


outfile.close()


##########

# opening the newly created file from  both

infile3 = open("training_control_labels.txt", "r")
lines_final = infile3.readlines()

total = lines_final[:]
#print(len(total))

# shuffling the lines
random.shuffle(total)

# creating new file to store shuffled  sequences from file above
outfile2 = open("training_control_labels_shuffled.txt", "w")  #794233 lines in seq_control_labels.txt
for i in total:
    outfile2.write(i)

outfile2.close()


########

infile = open("training_control_labels_shuffled.txt", "r") #794233 lines in seq_control_labels.txt
lines = infile.readlines()

total_shuffled = []

for i in lines:
    if "N" not in i:
        total_shuffled.append(i)
print(len(total_shuffled)) # 785595


# create file for labels
outfile = open("labels.txt", "w")  #785595 lines in lables.txt
for i in total_shuffled:
    outfile.write(i[0]+"\n")

outfile.close()

# create sequences for labels
outfile2 = open("sequences.txt", "w")  #785595 lines in sequences.txt
for i in total_shuffled:
    outfile2.write(i[1:])

outfile2.close()
