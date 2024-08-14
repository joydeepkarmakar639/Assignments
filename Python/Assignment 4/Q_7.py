def main():
    input_sequence = input("Enter a sequence of words separated by whitespace: ")
    words = input_sequence.split()
    digit_words = [word for word in words if word.isdigit()]
    print(digit_words)
if __name__ == "__main__":
    main()
