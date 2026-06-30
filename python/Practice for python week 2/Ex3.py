def longest(words):
    longest_word= words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
print(longest(["Hammad", "Azlan", "azan"]))
print(longest(["Jawad", "Num", "ali", "Abdullah"]))
print(longest(["Rana", "alyan", "Hamza"]))
