# Reverse translation mapping from codon to nucleotide triplets
reverse_table={
    'F':['TTT','TTC'],
    'L':['TTA','TTG','CTT','CTC','CTA','CTG'],
    'S':['TCT','TCC','TCA','TCG','AGT','AGC'],
    'Y':['TAT','TAC'],
    'B':['TAA','TAG','TGA'],
    'C':['TGT','TGC'],
    'W':['TGG'],
    'P':['CCT','CCC','CCA','CCG'],
    'H':['CAT','CAC'],
    'Q':['CAA','CAG'],
    'R':['CGT','CGC','CGA','CGG','AGA','AGG'],
    'I':['ATT','ATC','ATA'],
    'M':['ATG'],
    'T':['ACT','ACC','ACA','ACG'],
    'N':['AAT','AAC'],
    'K':['AAA','AAG'],
    'V':['GTT','GTC','GTA','GTG'],
    'A':['GCT','GCC','GCA','GCG'],
    'D':['GAT','GAC'],
    'E':['GAA','GAG'],
    'G':['GGT','GGC','GGA','GGG']
}
# Read file of offset codon sequences
file = open('sequences.txt')
# Replace STOP with an arbitrary key ('B') since we want to iterate over every codon considered as 1 character
lines = file.read().replace('STOP','B').splitlines()
# Iterate over every 4 lines which correspond to the gene and its 3 codon sequences
for gene in range(len(lines)//4):
    # Extract first sequence
    first = lines[gene*4+1]
    # Extract second sequence
    second = lines[gene*4+2]
    # Extract third sequence
    third = lines[gene*4+3]        
    possibilities=[]
    outputs=['']
    # Iterate over all genes except for the last
    for i in range(len(first)-1):
        # Candidates for the i'th gene are taken from the first sequence's i'th gene
        candidates = reverse_table[first[i]]
        # Eliminate candidates where the second sequence's i'th gene's first and second nucleotides don't match the
        # candidate's second and third nucleotides
        candidates = [candidate for candidate in candidates if candidate[1] in [seq[0] for seq in reverse_table[second[i]]]]
        candidates = [candidate for candidate in candidates if candidate[2] in [seq[1] for seq in reverse_table[second[i]]]]
        # Eliminate candidates where the third sequence's i'th gene's first nucleotide doesn't match the candidate's third nucleotide
        candidates = [candidate for candidate in candidates if candidate[2] in [seq[0] for seq in reverse_table[third[i]]]]
        if len(possibilities)>0:
            candidates = [candidate for candidate in candidates if candidate[0] in possibilities]
                    
        filtered=[]
        for candidate in candidates:
            for seq in reverse_table[second[i]]:
                if seq[0:2] == candidate[1:3]:filtered.append(seq)
            possibilities=[]
            for seq in reverse_table[third[i]]:
                if seq[0] == candidate[2]:
                    for possibility in filtered:
                        if seq[1] == possibility[2] and seq[1] not in possibilities :
                            possibilities.append(seq[1])
        temp=[]
        for output in outputs:
            for candidate in candidates:
                temp.append(output+candidate)
        outputs=temp
    last = reverse_table[first[len(first)-1]]
    last = [candidate for candidate in last if candidate[0] in [seq[2] for seq in reverse_table[second[len(second)-1]]]]
    last = [candidate for candidate in last if candidate[0:2] in [seq[1:3] for seq in reverse_table[third[(len(third)-1)]]]]
    print(lines[gene*4])
    if len(outputs)==1: 
        if len(last)<1:
            print('No Solution found for last gene. This means initial sequence was missing amino acids and they were not a multiple of 3.')
            print('Found unique solution for all other previous genes.')
            print('Solution: '+outputs[0])
        elif len(last)==1:
            print('Found unique solution for all genes')
            print('Solution : '+outputs[0]+last[0])
        else:
            print('Found unique solution for all but last gene')
            print('Solution : '+outputs[0])
            print('Last gene possibilities: '+str(last))
    else:
        temp=[]
        for output in outputs:
            for final_aa in last:
                temp.append(output+final_aa) 
        print('Multiple solutions found.')
        # print(temp)
        if len(last)<1:print('No Solution found for last gene. This means initial sequence was missing amino acids and they were not a multiple of 3.')
    print()