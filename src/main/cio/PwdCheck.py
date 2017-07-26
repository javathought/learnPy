checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    )

# res = 0
# # replace this for solution
# for d in data:
#     if d.islower():
#         res |= 1
#     if d.isupper():
#         res |= 2
#     if d.isdigit():
#         res |= 4
#
# return res == 7 and len(data) >= 10


print('qwerty345'.isalpha())

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('qwerty911911') == False, "6th example"