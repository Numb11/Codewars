def decode_morse(morse_code):
 deciphered = []
 words = morse_code.split('   ')
 for x in range(len(words)):
    for i in words[x].split():
        deciphered.append(MORSE_CODE[i])
    deciphered.append(' ')
 return(''.join(deciphered).strip())
