class Solution:
    def maskPII(self, s: str) -> str:
        result = ""
        if "@" in s:
            # email
            symbol_index = s.index("@")
            result = (
                s[0].lower()
                + "*****"
                + s[symbol_index - 1].lower()
                + s[symbol_index:].lower()
            )
        else:
            # phone number
            valid_number = ""
            for d in s:
                if d.isdigit():
                    valid_number += d
            num_country_code = len(valid_number) - 10
            if num_country_code > 0:
                result = "+" + "*" * num_country_code + "-"
            result += "***-***-" + valid_number[-4:]

        return result
