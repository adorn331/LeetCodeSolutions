class Solution:
    def myAtoi(self, str):
        stripped = str.strip()
        if stripped == '' or not stripped[0].isdigit() and not stripped[0] in '-+':
            return 0
        for i in range(1, len(stripped)):
            if not stripped[i].isdigit():
                stripped = stripped[:i]
                break
        if stripped != '+' and stripped != '-':
            if -2147483648 <= int(stripped) <= 2147483647:
                return int(stripped)
            else:
                return 2147483647 if int(stripped) >= 2147483647 else -2147483648
        else:
            return 0
