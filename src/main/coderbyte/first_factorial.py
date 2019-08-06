def FirstFactorial(num):
    # code goes here
    fact = 1
    for i in range(2, num+1):
        fact = fact * i
    return fact


# keep this function call here
print FirstFactorial(int(raw_input()))
