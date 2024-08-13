import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo == None)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())
print(phoneRegex.search('My phone number is 555-1234. Call me tomorrow.'))
print(phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.'))

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
print(mo == None)

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said HaHaHa'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex.search('My numbers are 573-427-1033,404-7046,573-427-1033'))