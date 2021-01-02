import bs4 as bs
import requests
import json

def save_sp500_tickers():
    resp = requests.get("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find("table", {'class': 'wikitable sortable'})
    for row in table.findAll("tr")[1:]:
        ticker = row.findAll("td")[0].text
        tickers.append(ticker)

tickers =[]
save_sp500_tickers()
convertedlist = ["throwaway"]
for ticker in tickers:
    convertedlist.append(ticker.strip())

jsondump = json.dumps(convertedlist)
print(jsondump)