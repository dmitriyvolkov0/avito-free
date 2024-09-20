from bs4 import BeautifulSoup
import requests

# Парсим один запрос
def parse_data(page_number:int, text):
    url=f"https://www.avito.ru/all?cd=1&p={page_number}&q={text} бесплатно"

    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")

    items = bs.find_all("div", attrs={'data-marker': 'item'})

    results = []
    for item in items:
        title = item.find('h3', attrs={'itemprop': 'name'}).text
        price = int(item.find('meta', attrs={'itemprop': 'price'}).get('content'))
        url = 'https://avito.ru/' + item.find('a').get('href')

        if (price < 50) and (text in title):
            results.append({
                "title": title,
                "price": price,
                "url": url,
                "page_number": page_number
            })
    return results

def get_data_by_request(text:str):
    pages_count = 10
    results = []

    for page_number in range(1, pages_count+1):
        product = parse_data(page_number, text)
        results = results + product

    return {"results": results}