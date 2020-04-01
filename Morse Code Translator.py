#
# Name: Morse Code Translator
# Source: http://codereview.stackexchange.com/questions/15228/python-implementation-of-a-morse-code-translator
# Answered by: http://codereview.stackexchange.com/users/11728/gareth-rees
#
# Changes: removed python 2.x import from itertools izip
# Changed: python 2.x dict.iteritems() to dict.items()
#
# Usage : enter text with single space between words
#       : enter morse code with single space between letters and 2 spaces between words


def pairwise(s):
    """
    Generate pairs from the sequence `s`.

    >>> list(pairwise('abcd'))
    [('a', 'b'), ('c', 'd')]
    """
    it = iter(s)
    return zip(it,it)

morse_encoding = dict(pairwise('''
    a .-    b -...  c -.-.  d -..   e .     f ..-.  
    g --.   h ....  i ..    j .---  k -.-   l .-..
    m --    n -.    o ---   p .--.  q --.-  r .-.
    s ...   t -     u ..-   v ...-  w .--   x -..-
    y -.--  z --..

    1 .----   2 ..---   3 ...--   4 ....-   5 .....  
    6 -....   7 --...   8 ---..   9 ----.   0 -----

    , --..--  . .-.-.-  ? ..--..  / -..-.   - -....-
    ( -.--.   ) -.--.-  ' .----.  ! -.-.--  & .-...
    : ---...  ; -.-.-.  = -...-   + .-.-.   _ ..--.-
    " .-..-.  $ ...-..- @ .--.-.
    '''.split()))

morse_decoding = {v:k for k,v in morse_encoding.items()}

def is_morse_code(s):
    """
    Return True if the string `s` resembles Morse code (contains only
    dots, dashes and spaces), False otherwise.

    >>> is_morse_code('... --- ...')
    True
    >>> is_morse_code('abc')
    False
    """
    return set(s) <= set('.- ')

def morse_encode(s):
    """
    Encode the string `s` in Morse code and return the result. 
    Raise KeyError if it cannot be encoded.

    >>> morse_encode('morse code')
    '-- --- .-. ... .  -.-. --- -.. .'
    """
    return '  '.join(' '.join(morse_encoding[l] for l in word)
                    for word in s.lower().split(' '))

def morse_decode(s):
    """
    Decode the string `s` from Morse code and return the result.
    Raise KeyError if it cannot be decoded.

    >>> morse_decode('-- --- .-. ... .  -.-. --- -.. .')
    'morse code'
    """
    return ' '.join(''.join(morse_decoding[l] for l in word.split(' '))
                    for word in s.split('  '))

msg = input('MESSAGE: ')
if is_morse_code(msg):
    print(morse_decode(msg))
else:
    print(morse_encode(msg))
