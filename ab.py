consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def criteria(word):
    if len(word)>4:
        return False
    else:
        map = ''
        for letter in word:
            if letter in consonants:
                map = '1'+ map
            else:
                map = '0'+ map

        if len(word)==1 and not word=='a':
            return True
        if map=='10' or map=='01':
            return True
        if '11' in map or '101' in map:
            return True
        else:
            return False

def ab(string):
    return [word for word in string.lower().split(' ') if criteria(word)]