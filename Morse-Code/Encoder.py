morse_code = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.', 
    '.': '.-.-.-', 
    ',': '--..--', 
    '?': '..--..', 
    '!': '-.-.--', 
    '/': '-..-.', 
    ':': '---...', 
    ';': '-.-.-.', 
    '=': '-...-', 
    '+': '.-.-.', 
    '-': '-....-', 
    '_': '..--.-', 
    '"': '.-..-.', 
    '$': '...-..-', 
    '&': '.-...', 
    '@': '.--.-.'
}

def encoder(data):
    encoded_data = ""
    data = list(data.upper())
    for i in range(len(data)):
        encoded_data += morse_code[data[i]]
        encoded_data += " "
    return encoded_data

In = input("string: ")
print(encoder(In))
