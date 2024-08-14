def main():
    input_sentence = input("Enter a sentence: ")
    letters_count = 0
    digits_count = 0
    for char in input_sentence:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
    print("LETTERS", letters_count)
    print("DIGITS", digits_count)
if __name__ == "__main__":
    main()
