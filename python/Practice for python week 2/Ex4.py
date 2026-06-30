def count_vowels(text):
    count=0
    for char in text:
        if char in "aeiou":
            count +=1
    return count

print(count_vowels("Hammad"))
print(count_vowels("Abullah"))
print(count_vowels("awais"))