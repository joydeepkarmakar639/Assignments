def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    return s == s[::-1]
def ends_with(s, substring):
    return s.endswith(substring)
def capitalize_words(s):
    return s.title()
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])
def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)
def main():
    input_string = input("Enter a string: ")
    input_string = input_string.lower()
    print(f"Reversed string: {reverse_string(input_string)}")
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    specific_substring = input("Enter a specific substring to check if the string ends with it: ")
    if ends_with(input_string, specific_substring):
        print(f"The '{input_string}' ends with the substring '{specific_substring}'.")
    else:
        print(f"The '{input_string}' does not end with the substring '{specific_substring}'.")
    print(f"Capitalized string: {capitalize_words(input_string)}")
    
    string1 = input("Enter the first string to check for anagram: ")
    string1 = string1.lower()
    string2 = input("Enter the second string to check for anagram: ")
    string2 = string2.lower()
    
    if is_anagram(string1, string2):
        print(f"The strings '{string1}' and '{string2}' are anagrams.")
    else:
        print(f"The strings '{string1}' and '{string2}' are not anagrams.")
    print(f"String after removing vowels: {remove_vowels(input_string)}") 
    sentence = input("Enter a sentence to find the length of the longest word: ")
    print(f"Length of the longest word in the sentence: {longest_word_length(sentence)}")
if __name__ == "__main__":
    main()
