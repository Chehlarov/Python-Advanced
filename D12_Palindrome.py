def palindrome(word, idx):
    if word[idx] == word[len(word)-idx-1]:
        if idx >= len(word)-idx-1:
            return f"{word} is a palindrome"
        return palindrome(word, idx+1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("qabcba", 0))
