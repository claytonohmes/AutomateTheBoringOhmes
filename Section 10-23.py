#r'\d\d\d-\d\d\d-\d\d\d\d
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumRegex.search('My number is 573-427-1033'))
mo = phoneNumRegex.search('My number is 573-427-1033')
print(mo.group())
print(mo.group(1))
print(mo.group(2))


#now if you compile the regular expression with paratheses around the 
#areas of a regular expression that you want to have grouped you can do so
#with parenthesis.

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
yo = batRegex.search('Batmobile lost a wheel')
print(yo.group())

# if the seach method doesn't find it, then it will be none data type.