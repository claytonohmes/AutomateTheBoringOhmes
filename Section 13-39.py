import requests

responseObject = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(len(responseObject.text))

print(responseObject.text[:500])

BADresponseObject = requests.get('https://automatetheboringstuff.com/files/rjretds.txt')

#BADresponseObject.raise_for_status()

playfile = open('RomeoAndJuliet.txt', 'wb')

for chunk in responseObject.iter_content(10000):
    playfile.write(chunk)
