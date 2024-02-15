import random
import argparse
import sys

from scripts.timer import sleep_timer
from scripts.card import Card
from scripts import open_csv
from scripts.check_if_executed import check_executed



def main(path='xlsx/Vorlage.xlsx', output='xlsx/Ergebnis.xlsx', jump_over_filled=False, sleep_time=0, pause=True,
         concat=False, debug=False, word=False, word_text="Loading", dots=5, character="."):
    df = open_csv.read_csv(path)
    original = df.iloc[:, 9:].copy()
    num_rows = df['CM-Link'].count()
    df = df.iloc[:num_rows, :9]
    for index, row in df.iterrows():
        df = df.iloc[:num_rows, :9]

        # Skip if all values are already filled in or skip is set
        if jump_over_filled and str(row['Kartenname']) != "nan" or str(row['skip']) != "nan":
            print(f"    Skipping {index} because all values are already filled in or skip is set.")
            continue

        # Get the card from the url
        card = Card.with_url(row['CM-Link'])

        # Retry if card is None
        retries = 0
        while card is None:
            sleep_time = random.uniform(5.0, 8.0)
            if debug:
                print(f"Card with url {row['CM-Link']} is None. Retrying {retries} time(s) in {sleep_time} seconds.")
            sleep_timer(sleep_time, word=word, word_text=word_text, points=dots, character=character)
            if debug:
                print(f"Slept for {sleep_time} seconds")
            card = Card.with_url(row['CM-Link'])
            retries += 1

        # Print the current index and the total length of the dataframe
        print(f"{index} from {len(df)}")
        # Insert the values into the dataframe
        if debug:
            print(card)
        if concat:
            df = open_csv.concat(df, original)
        open_csv.insert_values(df, index, card)
        open_csv.save_to_excel(df, path=output)

        if index % 15 == 14 and pause:
            # Sleep for 10 seconds every 15 cards
            time = 10
            if debug:
                print(f"Sleeping for {time} seconds every 15 cards.")
            sleep_timer(time, word=word, word_text=word_text, points=dots, character=character)
        else:
            # Sleep for a random time between 0.5 and 1.5 seconds + the given sleep time
            anti_detection_sleep = random.uniform(sleep_time + 0.5, sleep_time + 1.5)
            if debug:
                print(
                    f"Sleeping for {anti_detection_sleep} seconds to "
                    f"not get detected by cardmarket.")
            sleep_timer(anti_detection_sleep, word=word, word_text=word_text, points=dots, character=character)
    if debug:
        print(df)
    print("Done")


if __name__ == "__main__":
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
    parser.add_argument('--concat', action='store_true',
                        help='Concatenates original with new. Removes all functions and hyperlinks. (Not clickable and instead of functions the text)')
    parser.add_argument('--pause', action='store_true', help='Pauses the execution after every 15 cards to prevent '
                                                             'detection by cardmarket. (default: True) Setting this flag disables the pause.')
    parser.add_argument('--debug', action='store_true', help='Debug mode')
    parser.add_argument('--word', action='store_true', help='Prints a word instead of dots')
    parser.add_argument('--word-text', type=str,
                        help='The word to print instead of dots (in combination with --word) or text instead of "Loading"')
    parser.add_argument('--dots', type=int, help='The amount of dots to print (default: 5)')
    parser.add_argument('--character', type=str, help='The character to print instead of dots')
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
    if args.pause:
        args.pause = False
    if args.create:
        open_csv.create_csv()
        sys.exit(1)
    if not args.concat:
        args.concat = False
    if not args.debug:
        args.debug = False
    else:
        print("Started with Args: ", args)
    if not args.word:
        args.word = False
    if not args.word_text:
        args.word_text = "Loading"
    if not args.dots:
        args.dots = 5
    if not args.character:
        args.character = "."

    main(path=args.path, output=args.output, jump_over_filled=args.jump_over_filled, sleep_time=args.sleep,
         pause=args.pause, concat=args.concat, debug=args.debug, word=args.word, word_text=args.word_text,
         dots=args.dots, character=args.character)
