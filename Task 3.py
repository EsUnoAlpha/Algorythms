def jewelry(jewels, stones):
    counter = 0
    for i in jewels:
        for n in stones:
            if i == n:
                counter += 1
    return counter

