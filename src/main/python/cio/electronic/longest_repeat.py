def repeat_inside(line):
    """
        first the longest repeating substring
    """
    # your code here

    longest = ''

    l = len(line)

    for i in range(l):
        if len(longest) >  l - i:
            break;
        for j in range(i+1, l):
            sub = line[i:j]
            sub_len = j-i
            cur_long = ''
            for k in range(j, l, sub_len):
                if line[k:k+sub_len] == sub:
                    cur_long += sub
                else:
                    break
            if len(cur_long) > 0:
                cur_long += sub
            if len(cur_long) > len(longest):
                longest = cur_long
    return longest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
