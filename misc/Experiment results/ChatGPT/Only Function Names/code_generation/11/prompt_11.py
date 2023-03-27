from typing import List


def string_xor(a: str, b: str) -> str:
    # Convert the strings to bytes
    a_bytes = bytes(a, 'utf-8')
    b_bytes = bytes(b, 'utf-8')
    # Initialize a empty result string
    result = ""
    # Iterate through the bytes of both strings
    for a_byte, b_byte in zip(a_bytes, b_bytes):
        # Perform the XOR operation and convert the result to a character
        result += chr(a_byte ^ b_byte)
    return result
