import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    element = soup.select('#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span:nth-child(2)')
    return element[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/ANRABESS-Cardigan-Sweater-715kaqi\
                       -M-Apricot/dp/B0BCPKQBXV/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.s\
                       ym.c4bb7dba-11f3-470a-9b96-c2d1f98f1b6f&pd_rd_r=30740a98-674d-4b36-a8fc-b\
                       bc4c7d350e1&pd_rd_w=rOlHg&pd_rd_wg=6hUN3&pf_rd_p=c4bb7dba-11f3-470a-9b96-c2d1f\
                       98f1b6f&pf_rd_r=QHKRCZEYD7WMS44ZRGZ6&qid=1699308502&s=apparel&sr=1-1')

#soup = bs4.BeautifulSoup(res.text, 'html.parser')
print('the price is ' + price)