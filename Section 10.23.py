import re
"""a function to recognize text without using regular expressions:
def isPhoneNumber(text):
    if len(text) != 12:
        return False #not a phone number
    for i in range (0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False #missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # Missing Last 4 digits
    return True

print(isPhoneNumber('573427-1033'))

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')"""

#how to do this function with a regular expression
message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'

#\d is for a digit and the r indicates a raw string so the \
# slashes don't become escape characters
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#this method returns a match object (called mo here)
mo = phoneNumberRegex.search(message)
print(mo.group())

#we can use the find all method instead to find every occurance: \
# stores it in a list
print(phoneNumberRegex.findall(message))

