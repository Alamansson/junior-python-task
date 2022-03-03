

def calculate_characters(quote: str) -> int:
    return len(quote.replace(' ', ''))


def calculate_vowels(quote: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    quote = quote.replace(' ', '').lower()
    vowel_count = [i for i in quote if i in vowels]
    return len(vowel_count)


def calculate_consonants(quote: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    quote = quote.replace(' ', '').lower()
    consonant_count = [i for i in quote if i not in vowels]
    return len(consonant_count)


def repeated_characters(quote: str) -> dict:
    import collections
    quote = quote.replace(' ', '').lower()
    frequencies = collections.Counter(quote)
    repeated = {}
    for key, value in frequencies.items():
        if value >= 1:
            repeated[key] = value
    return repeated


def average_length(quote: str) -> float:
    from statistics import mean
    quote = [len(i) for i in quote.split()]
    return round(mean(quote), 2)


def longest_word(quote: str) -> list:
    longest_words = []
    quotes = quote.split()
    for i in range(3):
        longest = quotes.pop(quotes.index(max(quotes, key=len)))
        longest_words.append(longest)
    return longest_words









