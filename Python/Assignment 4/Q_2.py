def main():
    input_sequence = input("Enter a comma-separated sequence of words: ")
    words = input_sequence.split(',')
    words.sort()
    sorted_sequence = ','.join(words)
    print("Sorted sequence:", sorted_sequence)
if __name__ == "__main__":
    main()
