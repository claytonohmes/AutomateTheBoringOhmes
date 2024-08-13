import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('Email@gmail.com','Password')
conn.select_folder('INBOX', readonly=True)

UIDs = conn.search('SINCE 20-AUG-2015')
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])
