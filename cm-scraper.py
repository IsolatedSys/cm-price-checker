import random
import argparse
import sys

from time import sleep
from scripts.card import Card
from scripts import open_csv
from scripts.check_if_executed import check_executed


def main(path='xlsx/Vorlage.xlsx', output='xlsx/Ergebnis.xlsx', jump_over_filled=False, sleep_time=0, pause=False):
    print(path, jump_over_filled)

    df = open_csv.read_csv(path)
    for index, row in df.iterrows():
        # Print the current index and the total length of the dataframe
        print(f"{index} from {len(df)}")

        # Skip if all values are already filled in or skip is set
        if jump_over_filled and str(row['Kartenname']) != "nan" or str(row['skip']) != "nan":
            print(f"Skipping {index} because all values are already filled in or skip is set.")
            continue

        # Get the card from the url
        card = Card.with_url(row['CM-Link'])

        # Retry if card is None
        retries = 0
        while card is None:
            sleep_time = random.uniform(5.0, 8.0)
            print(f"Card with url {row['CM-Link']} is None. Retrying {retries} time(s) in {sleep_time} seconds.")
            sleep(sleep_time)
            print(f"Slept for {sleep_time} seconds")
            card = Card.with_url(row['CM-Link'])
            retries += 1

        # Insert the values into the dataframe
        print(card)
        open_csv.insert_values(df, index, card)
        open_csv.save_to_excel(df, path=output)

        if index % 15 == 0 and index != 0 and pause:
            # Sleep for 10 seconds every 15 cards
            print(f"Sleeping for {(time := 10)} seconds every 15 cards.")
            sleep(time)
        else:
            # Sleep for a random time between 0.5 and 1.5 seconds + the given sleep time
            print(
                f"Sleeping for {(anti_detection_sleep := random.uniform(sleep_time + 0.5, sleep_time + 1.5))} seconds to "
                f"not get detected by cardmarket.")
            sleep(anti_detection_sleep)

    print(df)
    print("Done")


if __name__ == "__main__":
    print("Tested with default parameters, 47 cards in one run without any problems.")

    parser = argparse.ArgumentParser(description='Processes your card market links.')
    parser.add_argument('--path', type=str, help='Path to the input XLSX file')
    parser.add_argument('--output', type=str, help='Path to the out XLSX file')
    parser.add_argument('--jump_over_filled', action='store_true',
                        help='Jumps over filled entries and just scrape the new URLS (default: False)')
    parser.add_argument('--sleep', type=int,
                        help='Minimum time between requests (default: 3), the higher '
                             'the number the better the chance to not get detected by cardmarket the less retries are '
                             'needed')
    parser.add_argument('--create', action='store_true', help='Creates a new csv file with default columns')
    parser.add_argument('--pause', action='store_true', help='Pauses the execution after every 15 cards to prevent '
                                                             'detection by cardmarket. (default: True)')
    args = parser.parse_args()

    if not check_executed():
        print("First time executed. Read the help to get started.\n")
        parser.print_help()
        sys.exit(0)

    if not args.path:
        args.path = 'xlsx/Vorlage.xlsx'
    if not args.output:
        args.output = 'xlsx/Ergebnis.xlsx'
    if not args.jump_over_filled:
        args.jump_over_filled = False
    if not args.sleep:
        args.sleep = 3
    if not args.pause:
        args.pause = True
    if args.create:
        open_csv.create_csv()
        sys.exit(1)

    print("Started with Args: ", args)

    main(path=args.path, output=args.output, jump_over_filled=args.jump_over_filled, sleep_time=args.sleep, pause=args.pause)
