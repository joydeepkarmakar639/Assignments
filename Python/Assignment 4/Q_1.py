def main():
    input_string = "India is my motherland. I love my country. Capital of India is New Delhi."
    length_of_string = len(input_string)
    print(f"Length of the string: {length_of_string}")
    substring = "country"
    if substring in input_string:
        print(f'The substring "{substring}" is found in the string.')
    else:
        print(f'The substring "{substring}" is not found in the string.')
    cleaned_string = input_string.lower().replace('.', '').replace(',', '')
    words = cleaned_string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print("Occurrences of each word in the given sentence:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()
