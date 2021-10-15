# https://www.youtube.com/watch?v=PIeiiceWe_w&ab_channel=Cl%C3%A9mentMihailescu


def is_subseq(phone_number, word):
    pointer = 0
    for number in phone_number:
        if word[pointer] == number:
            pointer += 1
        if pointer == len(word):
            return True
    return False


def PhoneNumberLetterSubstring(phone_number, word_list):
    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    
    numeric_word_list = []
    # O(total chars in words)
    for word in word_list:
        numeric_word = ""
        for char in word:
            for key in letters:
                if char in letters[key]:
                    numeric_word += key
                    break
        numeric_word_list.append(numeric_word)

    # O(length of words * length of phone number *)
    return [
        word_list[i]
        for i in range(len(numeric_word_list))
        if is_subseq(phone_number, numeric_word_list[i])
    ]


phoneNumber = "3662277"
words = ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]
print(PhoneNumberLetterSubstring(phoneNumber, words))
