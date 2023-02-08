import sys
import os

# put arguments except for call argument in an array
args = sys.argv[1:]
# initialize paths array
paths = ['','','']
# any argument given is put into the paths array
for i in range(len(args)):
    paths[i]=args[i]
# check if the path to query sequence has been provided.
# if not, request it from the user.
if paths[0] == '':
    paths[0]=input('Please enter the path to the query sequence file:')
# check if the path to the sequences to compare has been provided.
# if not, request it from the user.
if paths[1] == '':
    paths[1]=input('Please enter the path to the sequences to compare file:')
# loop through both paths and check if they are valid
for path in paths[:2]:
    if not(os.path.exists(path) and os.path.isfile(path)):
        print('Path not found or is not a file.')
        exit()
# read the first file
with open(paths[0]) as file:
    original=file.read().split('>')[1:]
# create header and sequence variables
header=original[0].split('\n')[0]
amino_acids=original[0][len(header):].replace('\n','')

# read the second file and ommit the header
with open(paths[1]) as file:
    sequences = file.read().splitlines()[1:]
# find the length of longest and shortest sequence and compare them
if len(max(sequences,key=len))-len(min(sequences,key=len))>3:
    print('Sequences length too far')
    exit()

# set up an array to hold each sequence data
counts=[]

# loop through the sequences taking into consideration their index
for i,sequence in enumerate(sequences):
    # set up an array that includes:
    # a dictionary that holds the count of similar nucleotides
    # the sequence itself
    similar_count=[{'A':0,'C':0,'G':0,'T':0},sequence]
    # loop through every nucleotide
    for j in range(len(sequence)):
        # check if the nucleotide in the sequence matches the nucleotide in the original sequence (taking into consideration the offset)
        if sequence[j]==amino_acids[i+j]:similar_count[0][sequence[j]]+=1
    # add the array to the counts holder array
    counts.append(similar_count)
# sort the sequences according to the sum of count of similar nucleotides
# the key is a function that replaces the array by the value of the sum of values of the dictionary
# the reverse=True sorts the array in descending order
sorted_sequences = sorted(counts,key=lambda count: sum(count[0].values()),reverse=True)
# if a target file has not been provide it, prompt the user for it
if paths[2] == '':
    paths[2] = input('Please input destination file path(leave empty if not desired): ')
# if the path is not a file or not given, replace it with default path
paths[2] = paths[2] if paths[2]!='' else 'orderedSequences.fasta'
with open(paths[2],'w+') as file:
    for sequence in sorted_sequences:
        # for every sequence, write its header and its sequence
        current_header = '>'+header+'\tTotal Matching Score:'+\
                   str(sum(sequence[0].values()))+'/'+str(len(sequence[1]))+\
                   '\tA:'+str(sequence[0]['A'])+\
                   '\tC:'+str(sequence[0]['C'])+\
                   '\tG:'+str(sequence[0]['G'])+\
                   '\tT:'+str(sequence[0]['T'])+\
                   '\n'
        print(current_header)
        file.write(current_header)
        file.write(sequence[1]+'\n')
