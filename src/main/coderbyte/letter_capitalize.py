def LetterCapitalize(str):
    # code goes here
    return " ".join([word.capitalize() for word in str.split(" ")])


# keep this function call here
print LetterCapitalize(raw_input())


