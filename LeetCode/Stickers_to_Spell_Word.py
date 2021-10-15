# https://leetcode.com/problems/stickers-to-spell-word/
class Solution:
    def minStickers(self, stickers, target):
        def string_to_list(s):
            target_dict = {}
            for char in s:
                if char not in target_dict:
                    target_dict[char] = 0
                target_dict[char] += 1
            return target_dict

        total_set = set("".join(stickers))
        target_set = set(target)

        if not target_set.issubset(total_set):
            return -1

        target_dict = string_to_list(target)

        target_list = sorted(list([*target_dict]))
        # target_list = [*target_dict]
        initized_string = ""
        target_string = ""
        for i in target_list:
            target_string += i + str(target_dict[i]) + "-"
            initized_string += i + "0-"

        total_set = set()
        total_set.add((initized_string, 0))

        temp_stickers = []
        temp_str_dict = []
        for i in stickers:
            temp_i = ""
            for j in i:
                if j in target:
                    temp_i += j
            if len(temp_i) != 0:
                temp_stickers.append(temp_i)
                temp_str_dict.append(string_to_list(temp_i))

        result = float("inf")
        not_updated = True
        while not_updated:
            not_updated = True
            for i, str_dict in zip(temp_stickers, temp_str_dict):
                cur_set = set()
                for string, counter in total_set:
                    if string == target_string:
                        continue
                    changed = False
                    for char in str_dict:
                        if char in target_dict:
                            char_index = string.index(char) + 1
                            end_index = string[char_index:].index("-") + char_index
                            acc_counter = (
                                int(string[char_index:end_index]) + str_dict[char]
                            )
                            acc_counter = min(acc_counter, target_dict[char])
                            string = (
                                string[:char_index]
                                + str(acc_counter)
                                + string[end_index:]
                            )
                            changed = True

                        if changed:
                            if string == target_string:
                                result = min(result, counter + 1)
                                not_updated = False
                                break
                            cur_set.add((string, counter + 1))
                if not not_updated:
                    break
                # total_set = total_set.union(cur_set)
                total_set = cur_set
                print(total_set)
        print(total_set)
        return result


stickers = ["with", "example", "science"]
target = "thehat"
# stickers = ["notice", "possible"]
# target = "basicbasic"
# stickers = ["these", "guess", "about", "garden", "him"]
# target = "atomher"

stickers = ["fly", "me", "charge", "mind", "bottom"]
target = "centorder"

stickers = ["bring", "plane", "should", "against", "chick"]
target = "greatscore"

stickers = [
    "fair",
    "bell",
    "wall",
    "spring",
    "energy",
    "measure",
    "it",
    "walk",
    "past",
    "heard",
    "street",
    "human",
    "village",
    "best",
    "clock",
    "make",
    "shall",
    "visit",
    "two",
    "ran",
    "between",
    "has",
    "hat",
    "over",
    "begin",
    "that",
    "may",
    "direct",
    "step",
    "made",
    "trouble",
    "stay",
    "glad",
    "arrange",
    "both",
    "protect",
    "land",
    "noun",
    "name",
    "organ",
    "level",
    "might",
    "hunt",
    "cover",
    "heat",
    "motion",
    "can",
    "rock",
    "operate",
    "spend",
]
target = "firstthick"

stickers = [
    "among",
    "right",
    "picture",
    "bell",
    "an",
    "distant",
    "left",
    "carry",
    "speed",
    "continent",
    "few",
    "snow",
    "port",
    "machine",
    "paint",
    "much",
    "finger",
    "pretty",
    "build",
    "poor",
    "then",
    "begin",
    "evening",
    "branch",
    "syllable",
    "tool",
    "burn",
    "molecule",
    "step",
    "letter",
    "trade",
    "world",
    "consonant",
    "now",
    "with",
    "grow",
    "protect",
    "substance",
    "science",
    "sand",
    "green",
    "either",
    "each",
    "very",
    "position",
    "quotient",
    "root",
    "agree",
    "wind",
    "usual",
]
target = "basicforce"

sol = Solution()
print(sol.minStickers(stickers, target))

# ["bring", "plane", "should", "against", "chick"]
# "ain", "bing", "bing", "plan", "plan", "shuld", "hick"
