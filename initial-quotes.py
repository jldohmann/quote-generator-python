from lxml import html
import requests
import json

page = requests.get('https://en.wikiquote.org/wiki/Stephen_Wolfram')
tree = html.fromstring(page.content)

quotes = tree.xpath('//div[@class="mw-parser-output"]/ul/li/text()')
quotes_clean = quotes[0:15]

data = dict(enumerate(quotes_clean, start=1))
data = {'quotes': data}

with open('quotes.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)
