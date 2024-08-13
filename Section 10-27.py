import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello There'))
print(beginsWithHelloRegex.search('He said "Hello!"') == None)

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('123412736489273676458972634523645953481'))
print(allDigitsRegex.search('1873016450176340610578614x186375') == None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

#the dot star syntax means anything whatsoever

name = 'First Name: Al Last Name: Sweigart'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(name))
#dot star uses greedy. To use it non greedy you use a quesiton mark.

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


