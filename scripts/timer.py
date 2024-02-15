from time import sleep


def sleep_timer(sleep_time, points=5, character=".", word=False, word_text="Loading"):
    time = int(sleep_time * points)
    exploded = explode_word(word_text)
    for x in range(0, time):
        if word:
            if x % (word_text.__len__()) == 0 and x!=0:
                print("", end="\r")
                exploded = explode_word(word_text)
            else:
                print(exploded.__next__(), end="")
        else:
            if x % (points + 1) == 0:
                print("", end="\r")
                print(word_text, end="")
            else:
                print(character, end="")
        sleep(1 / points)
    print("", end="\r")

def explode_word(word_text):
    '''Explodes a word into a list of characters'''
    yield from word_text