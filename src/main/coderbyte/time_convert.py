def TimeConvert(nums):
    # code goes here
    num = int(nums)
    return str(num//60) + ':' + str(num % 60)


# keep this function call here
print(TimeConvert(input()))
