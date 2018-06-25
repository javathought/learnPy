def sun_angle(time):
    #replace this for solution
    total_min = 12 * 60
    hour, min = map (int, time.split(':'))
    if (hour < 6 or hour > 18 or hour == 18 and min > 0):
        return "I don't see the sun!"
    mins = (hour - 6) * 60 + min

    return mins / total_min * 180

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("18:01") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")