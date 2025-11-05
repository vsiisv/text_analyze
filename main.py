import string


def remove_punctuation(text):
    punctuation = string.punctuation
    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text


def get_most_long_word(list_of_words):
    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def get_vowels_count(text):
    vowels_count = 0
    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for vowel in text:
        if vowel in vowels:
            vowels_count += 1

    return vowels_count


def get_count_repeated_words(list_of_words):
    dictionary = {}
    for word in list_of_words:
        dictionary[word] = dictionary[word] + 1 if word in dictionary else 1

    return dictionary


def output_format(dict_of_words):
    print("Слова, по количеству повторений:")
    for word, count in dict_of_words.items():
        print(f"{word}: {count}")


def main():
    text = input("Введите текст: ").lower()
    list_of_words = text.split()

    text = remove_punctuation(text)
    words_count = len(list_of_words)
    most_long_word = get_most_long_word(list_of_words)
    vowels_count = get_vowels_count(text)
    repeated_words = get_count_repeated_words(list_of_words)

    print(f"""
        Количество слов в тексте: {words_count}
        Самое длинное слово: {most_long_word}
        Количество гласных: {vowels_count}
    """)
    output_format(repeated_words)


main()
