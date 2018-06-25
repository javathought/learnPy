import pandas as pd
from collections import Counter
import string


def checkio_opt(text):
    return max(string.ascii_lowercase, key = text.lower().count)



def checkio(text):
    # replace this for solution

    freqs = {}

    letters = [l for l in text.lower() if 'a' <= l <= 'z']


    dfLetters = pd.DataFrame({'letter' : letters})
    # print(dfLetters)
    count = dfLetters.groupby('letter').count()
    # print("*************** count")
    # print(count.max())
#                              'freq': 1})

    for l in letters:
        if l in freqs:
            freqs[l] = freqs[l] + 1
        else:
            freqs[l] = 1


    most = ('a', 0)

    for f in freqs:
        # print(freqs[f])
        if freqs[f] > most[1]:
            most = (f, freqs[f])
        elif freqs[f] == most[1] and f < most[0]:
            most = (f, freqs[f])

    return most[0]



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")