import time
prevTime = time.time()
prevClock = time.process_time()

# Read Data file
file = open('TransmembraneData.txt','r')

# Split data into rows
lines = file.read().splitlines()

# Close file since not needed anymore
file.close()

# Setup sets(not lists since sets like dicts use hashes with O(1) lookup time)
# Output being a set allows for removing duplicates
output=dict()

# Open duplicates file to write directly (no list needed for this)
duplicates = open('duplicateIntercations.txt','w+')

# Write header row
duplicates.write(lines[0]+'\n')

# Initialize counter for duplicate interactions
duplicateSum=0

# Loop through all lines after header
for line in lines[1:]:
    
    # The following line could be used to get rid of duplicates
    # if line in output.values():continue
    # However, since row duplicates contain the same interactions,
    # A row duplicate is inherently an interaction duplicate
    # Therefore, only checking for interaction duplicates is necessary
    
    # Take out necessary information from line
    args = line.split('\t')
    
    # Create a unique key that constitutes all necessary data that defines a unique interaction
    # The key will be hashed and stored in the interactions set
    key = args[1]+' '+args[4]+' '+args[7]+' '+args[8]+' '+args[10]+' '+args[13]+' '+args[16]+' '+args[17]
    
    # Create the reverse of the key for reverse compatibility
    invKey = args[10]+' '+args[13]+' '+args[16]+' '+args[17]+' '+args[1]+' '+args[4]+' '+args[7]+' '+args[8]
    
    # If the interaction and its reverse are not stored yet,
    if key not in output :
        if invKey not in output:
            output[key]=line
            continue
            
    # The line constitutes a duplicate interaction.
    # Write the line to the duplicates file
    duplicates.write(line+'\n')
    
    # Increment duplicate interaction counter
    duplicateSum+=1

# We're done writing to the duplicate interaction file
duplicates.close()

# Write all the unique interactions to a file
with open('uniqueInteractions.txt','w+') as out:
    out.write(lines[0]+'\n')
    for line in output.values():
        out.write(line+'\n')

# Print relevant information
print('Number of unique interactions: ',len(output))
print('Number of duplicate interactions: ',duplicateSum)
print('Execution time: ',time.time()-prevTime)
print('Clock time: ',time.process_time()-prevClock)
