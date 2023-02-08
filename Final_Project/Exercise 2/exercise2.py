import os
import time

prevTime = time.time()
prevClock = time.process_time()

# I already ran a script to get me all possible resNames in the entire folder.
# Setting up a list with them is much faster than dynamically creating them
resNames=['HIS', 'GLU', 'ILE', 'GLN', 'SER', 'LEU', 'LYS', 'VAL', 'TYR', 'PHE', 'GLY', 'ASN', 'ASP', 'ALA', 'PRO', 'CYS', 'TRP', 'ARG', 'THR', 'MET']

# Create a dictionary for all complementary interactions
# This creates our NxN matrix with the elements being sets
complements = dict()
for A in resNames:
    complements[A]=dict()
    for B in resNames:
        complements[A][B]=set()

# loop through all files in the folder
for file in os.listdir('PDBSumFiles'):
    # Read the file
    with open(os.path.join('PDBSumFiles',file),'r') as data:
        
        # Read data from the file and split it to lines
        data = data.read().splitlines()
        
        # Remove data before Header we're looking for
        # Skip 7 lines to get to the first row we require
        data = data[data.index('Non-bonded contacts')+7:]
        
        # Remove the data after an empty line signifying end of data required
        data = data[:data.index('')]
        
        # Loop through lines
        for line in data:
            # Split lines to fields delimited by spaces
            line = line.rsplit()
            
            # Add the interactions to both sides of the matrix
            complements[line[3]][line[9]].add(line[4]+'-'+line[10])
            complements[line[9]][line[3]].add(line[10]+'-'+line[4])
# Write the file
with open('interactionStatistics.txt','w+') as file:
    # First empty space. Using a string to build the row
    # since I need to remove the last tab and add a newline
    row = '\t'
    for name in resNames:
        row+=name+'\t'
    file.write(row[:-1]+'\n')
    # Loop through every row and column and insert the number
    # Of interactions there
    for rowName in resNames:
        row=rowName+'\t'
        for column in resNames:
            row+=str(len(complements[rowName][column]))+'\t'
        file.write(row[:-1]+'\n')
print('Number of files processed: ',len(os.listdir('PDBSumFiles')))
print('Run time: ',time.time()-prevTime)
print('Processing time: ',time.process_time()-prevClock)