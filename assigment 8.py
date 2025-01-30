def count_frequencies(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

numbers = [10, 40, 50, 14, 40, 10]
print(count_frequencies(numbers))

#The function returns a dict (dictionary).