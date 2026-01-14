
VOWELS = {'a', 'e', 'i', 'o', 'u', 'v'}
TONE_MARKS = {
    'a': ['ā', 'á', 'ǎ', 'à'],
    'e': ['ē', 'é', 'ě', 'è'],
    'i': ['ī', 'í', 'ǐ', 'ì'],
    'o': ['ō', 'ó', 'ǒ', 'ò'],
    'u': ['ū', 'ú', 'ǔ', 'ù'],
    'v': ['ǖ', 'ǘ', 'ǚ', 'ǜ']
}

def pinyin(input):
    '''
    Converts pinyin without tone marks to pinyin with tone marks.
    
    :param input: pinyin with number suffixes separated by spaces
    ex. zao3 shang4 hao3 zhong1 guo2
    '''
    words = input.split()

    result = []
    for word in words:
        try:
            is_valid(word)
        except ValueError:
            print("Invalid pinyin word: " + word)
            return ""
        tone = int(word[-1])
        token = word[:-1]
        result.append(add_tone(token, tone))
    return " ".join(result)

def is_valid(word):
    '''
    Checks whether the token is valid pinyin, in that it is a string of
    alphabetical characters containing at least one vowel suffixed by exactly
    one number from range 0 to 5 inclusive.

    ex. hao3 --> valid
        hao --> invalid
        h3 --> invalid
        hao6 --> invalid
    
    :param word: one pinyin word to check
    '''
    token = word[:-1]
    tone = word[-1]
    if token.isalpha() and tone.isdigit() and 0 <= int(tone) <= 6:
        for c in token:
            if c in VOWELS:
                return True
            
    raise ValueError("Word " + word + " is not valid")

def add_tone(token, tone):
    '''
    Adds the appropriate tone to the given token.
    
    :param token: one pinyin word
    :param tone: corresponding tone to add
    '''
    vowel_order = {
        'a':0,
        'e':1,
        'i':2,
        'o':3,
        'u':4,
        'v':5
    }

    # tone 5 has no tone mark
    if tone == 5:
        contains_v = token.find('v')
        if contains_v == -1:
            return token
        else:
            return token[:contains_v] + 'ü' + token[contains_v+1:]
    
    # find the vowel to be replaced (first vowel in order)
    first_vowel = 'v'
    argmax = -1
    for i in range(len(token)):
        c = token[i]
        if c in VOWELS:
            if vowel_order[c] <= vowel_order[first_vowel]:
                first_vowel = c
                argmax = i
    
    result = token[:argmax] + TONE_MARKS[first_vowel][tone - 1] + token[argmax+1:]
    return result


def main():
    print("enter pinyin:")
    print("example: zao3 shang4 hao3 zhong1 guo2")
    pinyin_in = input()
    print(pinyin(pinyin_in))
    return

if __name__ == "__main__":
    main()
