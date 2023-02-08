# Forward mapping from nucleotide triplet to codon
codon_table={
  'TTT' : "F", 'TTC' : "F", 'TTA' : "L", 'TTG' : "L",
  'TCT' : "S", 'TCC' : "S", 'TCA' : "S", 'TCG' : "S",
  'TAT' : "Y", 'TAC' : "Y", 'TAA' : "STOP", 'TAG' : "STOP",
  'TGT' : "C", 'TGC' : "C", 'TGA' : "STOP", 'TGG' : "W",
  'CTT' : "L", 'CTC' : "L", 'CTA' : "L", 'CTG' : "L",
  'CCT' : "P", 'CCC' : "P", 'CCA' : "P", 'CCG' : "P",
  'CAT' : "H", 'CAC' : "H", 'CAA' : "Q", 'CAG' : "Q",
  'CGT' : "R", 'CGC' : "R", 'CGA' : "R", 'CGG' : "R",
  'ATT' : "I", 'ATC' : "I", 'ATA' : "I", 'ATG' : "M",
  'ACT' : "T", 'ACC' : "T", 'ACA' : "T", 'ACG' : "T",
  'AAT' : "N", 'AAC' : "N", 'AAA' : "K", 'AAG' : "K",
  'AGT' : "S", 'AGC' : "S", 'AGA' : "R", 'AGG' : "R",
  'GTT' : "V", 'GTC' : "V", 'GTA' : "V", 'GTG' : "V",
  'GCT' : "A", 'GCC' : "A", 'GCA' : "A", 'GCG' : "A",
  'GAT' : "D", 'GAC' : "D", 'GAA' : "E", 'GAG' : "E",
  'GGT' : "G", 'GGC' : "G", 'GGA' : "G", 'GGG' : "G"
}
# Read fasta file
sequences = open('ACE2Sequences.fasta','r')
# Read the lines after header and iterate over each sequence separately
lines = sequences.read().split('>')[1:]
for sequence in lines:
    # Get the header
    header=sequence.split('\n')[0]
    # Create amino acid string
    amino_acids=sequence[len(header):].replace('\n','')
    print('\nSequence: '+header.split(' ')[0])
    print('Amino Acids: ' + amino_acids)
    # Iterate over every possible offset (0,1,2)
    for i in range(3):
        translation=''
        # Iterate over every neucleotide triplet, translate it to a codon, append it to the translation string
        for j in range(int(len(amino_acids[i:])/3)):
            translation+=codon_table[amino_acids[i+j*3:i+j*3+3]]
        print('\nTranslation '+str(i+1)+': '+translation)