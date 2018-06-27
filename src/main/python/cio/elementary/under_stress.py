import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if all([c.isupper() for c in subj if c.isalpha()]):
        return True

    if subj[-3:] == "!!!":
        return True

    words = re.sub(r'(.)(\1+)', r'\1', "".join([c.lower() for c in subj if c.isalpha()]))

    if "help" in words or "asap" in words or "urgent" in words:
        return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("HI .") == True, "Caps"
    assert is_stressful("Hi !!!") == True, "Exclamation"
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I neeed H-E-L-P") == True, "Second"
    assert is_stressful("I neeed HHHEEELP") == True, "Second"
    print('Done! Go Check it!')