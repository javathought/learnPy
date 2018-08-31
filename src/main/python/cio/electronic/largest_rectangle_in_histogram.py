def largest_histogram(histogram):
    s = [[0 for x in range(max(histogram))] for y in range(len(histogram))]
    max_surface = 0

    for i in range(0, len(histogram)):
        for h in range(0, histogram[i]):
            if s[i - 1][h] > 0 and i > 0:
                s[i][h] = s[i-1][h] + h+1
            else:
                s[i][h] = h+1
            if s[i][h] > max_surface :
                max_surface = s[i][h]

    return max_surface


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([2, 1, 4, 5, 2, 3, 3]) == 10, "complex 2"
    assert largest_histogram([2, 1, 4, 5, 3, 3, 3]) == 15, "complex 2"
    assert largest_histogram([2, 1, 4, 5, 4, 3, 3]) == 15, "complex 3"
    assert largest_histogram([2, 1, 4, 5, 5, 3, 3]) == 15, "complex 4"
    assert largest_histogram([2, 2, 4, 5, 2, 3, 3]) == 14, "complex 5"
    assert largest_histogram([2, 2, 4, 5, 2, 1, 3]) == 10, "complex 6"
    print("Done! Go check it!")