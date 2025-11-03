import string


def remove_punctuation(text):
    text = text.lower()
    punctuation = string.punctuation
    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text


def get_words_count(text):
    text = text.lower()
    count = 0
    for _ in text.split():
        count += 1

    return count


def get_most_long_word(text):
    words = text.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def get_vowels_count(text):
    text = text.lower()
    vowels_count = 0
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for vowel in text:
        if vowel in vowels:
            vowels_count += 1

    return vowels_count


def get_count_repeated_words(text):
    text = text.lower()
    words = text.split()
    dictionary = {}

    for word in words:
        dictionary[word] = dictionary[word] + 1 if word in dictionary else 1

    return dictionary


def output_format(list_of_words):
    for word, count in list_of_words.items():
        print(f"{word}: {count}")


def main():
    text = input("Введите текст: ")
    text = remove_punctuation(text)
    words_count = get_words_count(text)
    most_long_word = get_most_long_word(text)
    vowels_count = get_vowels_count(text)
    repeated_words = get_count_repeated_words(text)

    print(f"""
        Количество слов в тексте: {words_count}\n
        Самое длинное слово: {most_long_word}
        Количество гласных: {vowels_count}
    """)
    output_format(repeated_words)


main()
