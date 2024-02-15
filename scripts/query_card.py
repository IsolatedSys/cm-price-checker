import re
import cfscrape
from bs4 import BeautifulSoup
from my_fake_useragent import UserAgent

def query_card(url):
    while True:
        ua = UserAgent()
        user_agent = ua.random()
        scraper = cfscrape.create_scraper()
        scraper.headers['User-Agent'] = user_agent
        # print(scraper.headers['User-Agent'])
        # print(scraper.headers)
        response = ''
        try:
            response = scraper.get(url)
            scraper.close()
            return response.content
        except:
            continue


def extract_card_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')
    pattern = re.compile(r'(.*?) \(')
    if not h1:
        # print(html)
        return None

    match = re.search(pattern, h1.text)

    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        return None


def extract_card_number(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')
    pattern = re.compile(r'\((.*?)\)')
    if not h1:
        # print(html)
        return None
    match = re.search(pattern, h1.text)
    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        return None


def extract_price_map(html):
    ret = {}
    soup = BeautifulSoup(html, 'html.parser')
    info_div = soup.find('div', class_='info-list-container')
    try:
        dt_elements = info_div.find_all('dt', class_='col-6 col-xl-5')
        dd_elements = info_div.find_all('dd', class_='col-6 col-xl-7')
        for dt, dd in zip(dt_elements, dd_elements):
            dt_text = dt.get_text(strip=True)
            dd_text = dd.get_text(strip=True)
            ret[dt_text] = dd_text
        return ret
    except AttributeError:
        return None


if __name__ == '__main__':
    url = "https://www.cardmarket.com/de/Pokemon/Products/Singles/Lost-Origin/Galarian-Perrserker-V-V1-LOR129?language=3&minCondition=2"
    card_name = "Galar-Mauzinger V"
    card_number = "LOR 129"
    ab = "0,15 €"
    preistrend = "0,73 €"
    durchschnitt_monat = "0,77 €"
    durchschnitt_woche = "0,69 €"
    durchschnitt_tag = "0,57 €"

    html = query_card(url)

    price_map = extract_price_map(html)
    assert price_map['ab'] == ab
    assert price_map['Preis-Trend'] == preistrend
    assert price_map['30-Tages-Durchschnitt'] == durchschnitt_monat
    assert price_map['7-Tages-Durchschnitt'] == durchschnitt_woche
    assert price_map['1-Tages-Durchschnitt'] == durchschnitt_tag
    assert extract_card_name(html) == card_name
    assert extract_card_number(html) == card_number
