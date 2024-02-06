from scripts.query_card import query_card, extract_card_name, extract_card_number, extract_price_map


class Card:
    def __init__(self, name, number, price_map, url):
        self.name = name
        self.number = number
        if price_map:
            self.from_price = price_map['ab']
            self.trend_price = price_map['Preis-Trend']
            self.monthly_price = price_map['30-Tages-Durchschnitt']
            self.weekly_price = price_map['7-Tages-Durchschnitt']
            self.daily_price = price_map['1-Tages-Durchschnitt']
        self.url = url

    @classmethod
    def with_url(cls, url):
        html = query_card(url)
        name = extract_card_name(html)
        number = extract_card_number(html)
        price_map = extract_price_map(html)
        if not price_map:
            return None
        return cls(name, number, price_map, url)

    def __str__(self):
        return (f"___________________________\n"
                f"Name: {self.name}\n"
                f"Nummer: {self.number}\n"
                f"Preis ab: {self.from_price}\n"
                f"Trendpreis: {self.trend_price}\n"
                f"30-Tage-Durchschnitt: {self.monthly_price}\n"
                f"7-Tage-Durchschnitt: {self.weekly_price}\n"
                f"1-Tage-Durchschnitt: {self.daily_price}\n"
                f"URL: {self.url}\n"
                f"___________________________")


if __name__ == "__main__":
    url = "https://www.cardmarket.com/de/Pokemon/Products/Singles/Lost-Origin/Galarian-Perrserker-V-V1-LOR129?language=3&minCondition=2"
    card_name = "Galar-Mauzinger V"
    card_number = "LOR 129"
    price_map = {'ab': "0,15 €", 'Preis-Trend': "0,73 €", '30-Tages-Durchschnitt': "0,77 €",
                 '7-Tages-Durchschnitt': "0,69 €", '1-Tages-Durchschnitt': "0,57 €"}

    card = Card(card_name, card_number, price_map, url)
    assert card.from_price == "0,15 €"
    assert card.trend_price == "0,73 €"
    assert card.monthly_price == "0,77 €"
    assert card.weekly_price == "0,69 €"
    assert card.daily_price == "0,57 €"
    assert card.name == card_name
    assert card.number == card_number

    card_with_url = Card.with_url(url)
    # assert card_with_url.from_price == "0,15 €"
    # assert card_with_url.trend_price == "0,73 €"
    # assert card_with_url.monthly_price == "0,77 €"
    # assert card_with_url.weekly_price == "0,69 €"
    # assert card_with_url.daily_price == "0,57 €"
    print(card_with_url.from_price)
    print(card_with_url.trend_price)
    print(card_with_url.monthly_price)
    print(card_with_url.weekly_price)
    print(card_with_url.daily_price)
    assert card_with_url.name == card_name
    assert card_with_url.number == card_number
