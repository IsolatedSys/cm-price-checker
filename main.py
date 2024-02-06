import random
from time import sleep
from card import Card
import open_csv

jump_over_filled = True

if __name__ == "__main__":
    """
    1: look up csv file which rows does not have all values
    2: if all values are filled in, check if there are any changes, if yes, apply changes
    3:
    """

    path = 'cm_list_nur_urls.xlsx'
    df = open_csv.read_csv(path)

    cards = []
    for index, row in df.iterrows():
        if index % 15 == 1:
            print(f"Sleeping for {(time := 10)} seconds")
            sleep(time)
        if jump_over_filled and str(row['Kartenname']) != "nan":
            print(f"Skipping {index} because all values are already filled in")
            continue
        print(f"{index} from {len(df)}")
        card = Card.with_url(row['CM-Link'])
        retries = 0
        while card is None:
            retries += 1
            sleep_time = random.uniform(5.0, 8.0)
            print(f"Card with url {row['CM-Link']} is None. Retrying {retries} time(s) in {sleep_time} seconds.")
            sleep(sleep_time)
            print(f"Slept: {sleep_time} seconds")
            card = Card.with_url(row['CM-Link'])
        print(card)
        open_csv.insert_values(df, index, card)
        open_csv.save_to_excel(df, path)
        sleep(random.uniform(0.5, 1.5))

    print(df)
    print("Done")

