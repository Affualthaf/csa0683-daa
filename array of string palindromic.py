def find_palindromic_string(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words1 = ["abc", "car", "ada", "racecar", "cool"]
print(find_palindromic_string(words1))

