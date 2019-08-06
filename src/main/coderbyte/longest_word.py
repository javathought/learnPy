from __future__ import print_function


def is_longest(current, longest):
    if len(current) > len(longest):
        return current
    return longest


def LongestWord(sen):
    # code goes here
    longest = ""
    current = ""
    for c in sen:
        if c.isalnum():
            current += c
        else:
            longest = is_longest(current, longest)
            current = ""

    longest = is_longest(current, longest)
    return longest


# keep this function call here
print(LongestWord(raw_input()))
