class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        length = len(chars)

        while read < length:
            current_char = chars[read]
            count = 0

            # Inner loop: scan forward as long as characters match
            while read < length and chars[read] == current_char:
                read += 1
                count += 1

            # The inner loop finished. Write the character!
            chars[write] = current_char
            write += 1

            # Write the count if necessary
            if count > 1:
                s = str(count)
                times = len(s)
                for i in range(times):
                    chars[write] = s[i]
                    write += 1

        return write
        