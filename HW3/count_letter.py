def count_letters(wordlist, letter):
    count = 0
    for word in wordlist:
        if letter in word:
            count += 1
    return count


print(count_letters(['python', 'c++', 'c', 'scala', 'java'], 'c'))

