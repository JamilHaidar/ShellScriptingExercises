import re
import datetime

# Read file
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
found = re.finditer('^[a-zA-Z\s]{6,}\t[a-zA-Z\s]{2,4}\t[0-9]{4}([0-9])[0-9]{2}\\1\t(?!Dorms).*\t([0-9])\\2/[1|10|11|12].*',txt,re.MULTILINE)
# re.finditer returns an interator of match objects. Therefore we iterate through it and return the string of the matched object in an array using match.group()
matches = [match.group() for match in found]
# loop through all matched strings and compare the date of birth to current year leaving only ages above 45
matches = [match for match in matches if datetime.datetime.now().year-int(match[-4:])>45]
# loop through all matched strings and check if the first four digits of the ID are greater than 2017
matches = [match for match in matches if int(match.split('\t')[2][:4])>2017]
if len(matches)==0:
    print('No solution found.')
elif len(matches)==1:
    print('Unique solution found. Robber is',matches[0].split('\t')[1],matches[0].split('\t')[0]+'.')
else:
    print('Multiple suspects found:')
    for match in matches:print(match)
