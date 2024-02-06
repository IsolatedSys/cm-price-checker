import pandas as pd


def read_csv(path):
    xlsx_path = path
    df = pd.read_excel(xlsx_path)
    return df


def get_links(path):
    df = read_csv(path)
    return df["CM-Link"]


def clear_floats(price):
    """
    Should clear the floats from ' €' and change ',' to '.'
    :param price:
    :return:
    """
    return float(price.replace(' €', '').replace(',', '.'))


def insert_from_prices(path, prices):
    df = read_csv(path)
    df['CM-Preis ab'] = clear_floats(prices)
    return df


def insert_trend_price(path, prices):
    df = read_csv(path)
    df['CM-Trend'] = clear_floats(prices)
    return df


def insert_monthly_price(path, prices):
    df = read_csv(path)
    df['CM-30-Tage'] = clear_floats(prices)
    return df


def insert_names(path, names):
    df = read_csv(path)
    df['Kartenname'] = names
    return df


def insert_card_number(path, numbers):
    df = read_csv(path)
    df['Kartennummer'] = numbers
    return df


def save_to_excel(df, path="tmp.xlsx"):
    df.to_excel(path, index=False)


if __name__ == "__main__":
    path = '../xlsx/cm_list_nur_urls.xlsx'
    df = read_csv(path)
    insert_from_prices(path, [i for i in range(48)])
    print(get_links(path))

    df.to_excel("tmp.xlsx")


def insert_values(df, index, card):
    """
    Should insert the values of the card into the dataframe at the given index
    :param df: The dataframe used
    :param index: The index of the row to insert the values
    :param card: The card object to insert
    :return: The dataframe with the inserted values
    """
    print(f"Inserting values for {card.name} at index {index}")
    print(f"{card}")
    df.at[index, 'CM-Preis ab'] = clear_floats(card.from_price)
    df.at[index, 'CM-Trend'] = clear_floats(card.trend_price)
    df.at[index, 'CM-30-Tage'] = clear_floats(card.monthly_price)
    df.at[index, 'CM-7-Tage'] = clear_floats(card.weekly_price)
    df.at[index, 'CM-1-Tag'] = clear_floats(card.daily_price)
    df.at[index, 'Kartenname'] = str(card.name)
    df.at[index, 'Kartennummer'] = str(card.number)

    df.at[index, 'CM-Link'] = f'=HYPERLINK("{card.url}", "{card.url}")'
    return df


def create_csv():
    df = pd.DataFrame(columns=['CM-Link', 'Kartenname', 'Kartennummer', 'CM-Preis ab', 'CM-Trend', 'CM-30-Tage', 'CM-7-Tage', 'CM-1-Tag', 'skip'])
    df.to_excel('xlsx/Vorlage.xlsx', index=False)
    print("Created xlsx/Vorlage.xlsx")

