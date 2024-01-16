letters = [chr(x) for x in range(ord("a"), ord("z")+1) if chr(x) not in "aeiou"]

print(letters, end ="  ")

vowels = [chr(x) for x in range(ord("a"), ord("z")+1) if chr(x)  in "aeiou"]

print(vowels, end ="  ")

consonants = {chr(x) for x in range(ord("a"), ord("z")+1) if chr(x) not in "aeiou"}

print(consonants, end ="  ")

letters = vowels & consonants 