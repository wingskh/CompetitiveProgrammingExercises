# https://leetcode.com/problems/unique-morse-code-words/
# https://leetcode.com/problems/unique-morse-code-words/discuss/2437990/Python-oror-Easily-Understood-oror-Faster-than-99.7-oror-2-Lines

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_array = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        result = set()
        for word in words:
            word = word.lower()
            transformations = ""
            for chr in word:
                transformations += morse_code_array[ord(chr) - 97]
            result.add(transformations)
        return len(result)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_array = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len({''.join([morse_code_array[ord(chr) - 97] for chr in word]) for word in words})


words = ["gin", "zen", "gig", "msg"]
sol = Solution()
result = sol.uniqueMorseRepresentations2(words)
print(result)
