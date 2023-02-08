# Exercise 1

You need to write a script in Perl or Python that will compute the number of common nucleotides (they are 4 ACGT). YOU SHOULD BE CAREFUL TO DEAL WITH THE T AND U IN THE SEQUENCE.

Your script should deal with the following:
- It should read the query sequence from a file in FASTA format (so one file with one sequence that you wish to compare) (Sequence used for translation in assignment 1 of this week)
- It should read another file with multiple sequences that you wish to compare your query sequence with. (Reverse transcribed sequences you obtained from assignment 2 of this week)
- THE USER CAN EITHER SEND THE PATH TO THE TWO FILES WHEN RUNNING THE CODE DIRECTLY AND IF NOT YOU SHOULD ASK HIM TO ENTER THE PATH TO THE QUERY SEQUENCE FILE AND THEN TO THE SEQUENCES FILE HE WISHES TO COMPARE
- THE USER CAN ALSO PROVIDE THE NAME OF THE TARGET FILE ON THE COMMAND LINE WHEN RUNNING THE CODE OR ASK HIM TO ENTER IT LATER.
- The sequences length should be around the same length. 
- Since you had multiple reverse transcribed sequences, you can check then which one is the closest to the original sequence you translated in assignment 1 of this week.
- Compare the query sequence to each of the sequences in the second file (TAKING INTO CONSIDERATION THE FRAME 0,1 or 2) one position at a time and count the total number of similar nucleotides. 
- You should report how many total similar nucleotides per position, ie how many match by position again taking the FRAME INTO CONSIDERATION, there are and how many similar A, C, G, and T separately.
- You should then rank the sequences in file 2 from most similar to least similar and write them to a file ‘orderedSequences.txt’ in FASTA Format.
- You should include in the header of each sequence the Total matching score and the matching score for each nucleotide A, C, G, and T
