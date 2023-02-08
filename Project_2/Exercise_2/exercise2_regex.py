# Import libraries needed
import re
import datetime

# Set variables needed
MIN_ID_YEAR='2017'
MIN_AGE=45

# Read theftData file
with open('theftData.txt') as file:
    txt= file.read()

# Find all instances that match with regex pattern
# ^[a-zA-Z\s]{5,}\t means any the first column has more than 5 characters
# [a-zA-z\s]{2,4}\t means the second columns has 2 to 4 characters
# [0-9]{4} means 4 numbers (year), ([0-9]) means the 5th character is to be a number and saved
# [0-9]{2} means 2 more numbers and \\1 means the first group saved (which is the 5th character)
# (?!Dorms).* is a look ahead function that returns false to the match if 'Dorms' is within the 4th column
# ([0-9]) means the first digit of the day is to be saved, \\2 means the second digit should match the first digit,
# /[1|10|11|12] means the month should be one of the ones specified and .* continues to the end of the line
# the txt is read as one whole string so the ^ and $ do not match every row. This is why we add the parameter re.MULTILINE which
# takes into account \n to separate rows
found = re.finditer('^[a-zA-z\s]{5,}\t[a-zA-z\s]{2,4}\t[0-9]{4}([0-9])[0-9]{2}\\1\t(?!Dorms).*\t(.)\\2/[1|10|11|12].*',txt,re.MULTILINE)

# re.finditer returns an interator of match objects. Therefore we iterate through it and return the string of the matched object in an array using match.group()
matches = [match.group() for match in found]

# Calculate the minimum year date for person to be more than 45 years old 
min_date= str(datetime.datetime.now().year-MIN_AGE)

# Start dynamically creating a regex for finding the year
# Example: if the minimum year is 2305 then regex is ([0-1][0-9]{3}|2[0-2][0-9]{2}|230[0-4])
# The tens digit was not mentioned since subtracting 0 from the tens brings us to the previous hundreds which is already accounted for
birthyears='('
for i in range(4):
    # Keep the digits already accounted for
    year=min_date[:i]
    # Skip a digit that is 0
    if(min_date[i]=='0'):continue
    # Range for current digit is [0-(digit-1)]
    year+='[0-'+str(int(min_date[i])-1)+']'
    # Fill the rest of the digits with [0-9] except for the last one
    if i<3:year+='[0-9]{'+str(4-i-1)+'}'
    # Add the year to the regex string and add a pipe
    birthyears+=year+'|'

# Remove last pipe and add closing bracket
birthyears = birthyears[:-1]+')'

# Filter in all matches that are before current date - minimum age
matches = [match for match in matches if re.match('.*\t.*\t.*\t.*\t.*/.*/'+birthyears,match)]

# Start dynamically creating a regex for finding the ID year
# Example: if the minimum year is 1976 then regex is ([2-9][0-9]{3}|19[8-9][0-9]{1}|197[7-9])
# The hundreds digit was not mentioned since adding 9 from the hundreds brings us to the next thousands which is already accounted for
years='('
for i in range(4):
    # Keep the digits already accounted for
    year=MIN_ID_YEAR[:i]
    # Skip a digit that is 9
    if(MIN_ID_YEAR[i]=='9'):continue
    # Range for current digit is [(digit+1)-9]
    year+='['+str(int(MIN_ID_YEAR[i])+1)+'-9]'
    # Fill the rest of the digits with [0-9] except for the last one
    if i<3:year+='[0-9]{'+str(4-i-1)+'}'
    # Add the year to the regex string and add a pipe
    years+=year+'|'

# Remove last pipe and add closing bracket
years = years[:-1]+')'

# Filter out all matches that are before minimum id year
matches = [match for match in matches if re.match('.*\t.*\t'+years+'[0-9]{4}\t.*',match)]

if len(matches)==0:
    print('No solution found.')
elif len(matches)==1:
    print('Unique solution found. Robber is',matches[0].split('\t')[1],matches[0].split('\t')[0]+'.')
else:
    print('Multiple suspects found:')
    for match in matches:print(match)
