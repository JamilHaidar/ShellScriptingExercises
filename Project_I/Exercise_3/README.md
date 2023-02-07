# Exercise 3
The file Annotations.txt is a very large file with thousands of records. So don’t try to use cat to display it.

Use the head command with the appropriate parameter to print only the first line of the file.

Note the number/index of the column “code”

This column contains the codes/IDs of different files some of which contain the symbol “_” in them.

    - Use the awk command to print out the contents of the column “code” only and calculate the number of codes with the “_” symbol in them. You can use grep, wc  and piping for that with the appropriate options.

    -	Use the sed command to delete all the lines that have the symbol “_” in them and keep a backup copy of the initial file.

    -	Write a bash script that takes one argument, the path to the filtered file ie without symbol “_”, and that performs the following:

        -	Print out the total number of entries/rows/lines in the file excluding the title row.

        -	Ask the user to enter the name of a new directory to create, ex “filtered_data”. It should alert the user if the directory already exists so that he/she can enter again a new name without exiting the script. The command mkdir can be used to create a directory.

        -	Once the directory is created, prompt the user to enter a keyword search: examples to try are “Homo sapiens” and “Mus musculus” 

        -   Make sure the search for these keywords is CASE INSENSITIVE

        -   Loop through all the lines in the file and if the line contains the keyword, CASE INSENSITIVE, you should write the whole line to a new file. The new file should contain the title row (first line) followed by all the lines that match your keyword and it should be saved in the directory that was created. The name of the file should be the same as the keyword but should not include any space in it. For instance if you try “Homo sapiens”, the file name should Homo_sapiens.txt.

        -	Display the number of lines in the new created file.
