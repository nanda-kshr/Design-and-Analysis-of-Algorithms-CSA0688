def find_substrings(words):
    result = []
    for i, word in enumerate(words):
        for j, other in enumerate(words):
            if i != j and word in other:
                result.append(word)
                break
    return result

print(find_substrings(["mass", "as", "hero", "superhero"]))
print(find_substrings(["leetcode", "et", "code"]))
print(find_substrings(["blue", "green", "bu"]))