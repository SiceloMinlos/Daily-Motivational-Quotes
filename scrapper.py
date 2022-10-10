from requests_html import HTMLSession
import random

def scrapeData(tag):
    url = f'https://quotes.toscrape.com/tag/{tag}/'
    session = HTMLSession()
    response = session.get(url)

    quotes_list = []

    quotes = response.html.find("div.quote")
    
    for quote in quotes:
        qoutes_Dictionary = {
            "Quote" : quote.find("span.text", first=True).text.strip(),
            "Author" : quote.find("small.author", first=True).text.strip()
        }

        quotes_list.append(qoutes_Dictionary)

    return quotes_list

def random_quote():
    quotes = scrapeData("life")
    random_number = random.randint(0, len(quotes) - 1)
    return quotes[random_number]
