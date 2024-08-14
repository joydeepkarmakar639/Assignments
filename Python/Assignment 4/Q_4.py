def main():
    input_sequence = input("Enter a sequence of whitespace-separated words: ")
    words = input_sequence.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    sorted_sequence = ' '.join(sorted_words)
    print("Sorted sequence without duplicates:", sorted_sequence)
if __name__ == "__main__":
    main()
