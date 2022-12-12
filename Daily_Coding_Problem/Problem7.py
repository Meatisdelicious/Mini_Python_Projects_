# Problem #29

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to
# represent repeated successive characters as a single count and character. For example,
# the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded
# have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.

class Solution:
    def encode(self, message):
        encoded_message = ""
        i = 0
        # Iteration through the message until the end of the message --> Hence the len(msg)-1 <-> to msg[-1]
        while i <= len(message) - 1:
            count = 1
            # getting the character index
            ch = message[i]
            j = i
            while (j < len(message) - 1):
                if (message[j] == message[j + 1]):
                    count = count + 1
                    j = j + 1
                else:
                    break
            encoded_message = encoded_message + str(count) + ch
            i = j + 1
        return encoded_message

    def decode(self, s):
        output = ""
        num = ""
        for i in s:
            if i.isalpha():
                output += i * int(num)
                num = ""
            else:
                num += i
        return output


# Test program
ob = Solution()
message = "AAAABBBCCDAA"
print("encoded message :", ob.encode(message))
print("decoded message :", ob.decode(ob.encode(message)))
