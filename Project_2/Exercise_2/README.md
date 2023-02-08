# Exercise 2

To be done in Perl or Python and not bash so you need to look into running regular expression (regex) in Perl or Python.

Someone is stealing books from the library! 

However, instead of clues about where each person was, we have a list of information about 3000 individuals.

We know the following information about the robber:
- The last 4 digits of their ID start and end with the same number (ex: 5345)
- They don’t live in the dorms
- Their first name has between 2 and 4 characters
- Their last name has more than 5 characters
- They were born in January, October, November or December
- They are more than 45 years old
- Their birthday is two equal digits 
- That person joined LAU after 2017

Using these clues, you can narrow down the list of names to just one person, the robber. Note that the current year is 2020.

Find the name of the person and the regex you used for each step.

Note you must have the regex for each step. Even if you get down to 3 people and can visually see which person it is, it does not count. You should return one First Name and Last Name on the terminal.
 
# Note
I implemented a solution that uses regex to filter out most information, but to compare values of integers, used python.
I implemented another solution (exercise2_regex) which **ONLY** uses regular expressions, even to do the integer comparison!