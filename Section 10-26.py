import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, \
    6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

#here is how you create your own character classes:

vowelRegex = re.compile(r'[aeiouAEIOU]')

print(vowelRegex.findall(lyrics))

#here is how you would do it for 2 vowels in a row.

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall(lyrics))

#negative character classes using a ^

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall(lyrics))