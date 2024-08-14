def main():
    print("Enter multiple lines of text (type 'end' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == 'end':
            break
        lines.append(line)
    capitalized_lines = [line.upper() for line in lines]
    print("\nOutput:")
    for line in capitalized_lines:
        print(line)
if __name__ == "__main__":
    main()
