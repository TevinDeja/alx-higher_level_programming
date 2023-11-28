#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    current_char = chr(char_code)
    if current_char != 'q' and current_char != 'e':
        print(current_char, end='')
