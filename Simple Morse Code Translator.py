#
# Name: Simple Morse Code Translator
# Source: http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/
#

import re

CODE_OUT = {'A': '.-',      'B': '-...',    'C': '-.-.',
            'D': '-..',     'E': '.',       'F': '..-.',
            'G': '--.',     'H': '....',    'I': '..',
            'J': '.---',    'K': '-.-',     'L': '.-..',
            'M': '--',      'N': '-.',      'O': '---',
            'P': '.--.',    'Q': '--.-',    'R': '.-.',
            'S': '...',     'T': '-',       'U': '..-',
            'V': '...-',    'W': '.--',     'X': '-..-',
            'Y': '-.--',    'Z': '--..',

            '0': '-----',   '1': '.----',   '2': '..---',
            '3': '...--',   '4': '....-',   '5': '.....',
            '6': '-....',   '7': '--...',   '8': '---..',
            '9': '----.',

            ' ':'/',        '.':'.-.-.-',   ',':'--..--',
            ':':'---...',   '?':'..--..',   "'":'.----.',
            '-':'-....-',   '/':'-..-.',    '@': '.--.-.',
            '=':'-...-',    '(':'-.--.',    ')':'-.--.-',
            '+':'.-.-.'
          }

CODE_IN = { '.-'    :'A',   '-...'  :'B',   '-.-.'  :'C',
            '-..'   :'D',   '.'     :'E',   '..-.'  :'F',
            '--.'   :'G',   '....'  :'H',   '..'    :'I',
            '.---'  :'J',   '-.-'   :'K',   '.-..'  :'L',
            '--'    :'M',   '-.'    :'N',   '---'   :'O',
            '.--.'  :'P',   '--.-'  :'Q',   '.-.'   :'R',
            '...'   :'S',   '-'     :'T',   '..-'   :'U',
            '...-'  :'V',   '.--'   :'W',   '-..-'  :'X',
            '-.--'  :'Y',   '--..'  :'Z',

            '-----' :'0',   '.----' :'1',   '..---' :'2',
            '...--' :'3',   '....-' :'4',   '.....' :'5',
            '-....' :'6',   '--...' :'7',   '---..' :'8',
            '----.' :'9',

            '/'     :' ',   '.-.-.-':'.',   '--..--':',',
            '---...':':',   '..--..':'?',   '.----.':"'",
            '-....-':'-',   '-..-.' :'/',   '.--.-.':'@',
            '-...-' :'=',   '-.--.' :'(',   '-.--.-':')',
            '.-.-.' :'+',   '-.-.--':'!',   '---.'  :'!'
          }

def main():
    msg = input('MESSAGE: ')
    if re.match("[.-/]",msg):
        matchObj = re.match('[.-]{1,5}(?> [.-]{1,5})*(?>   [.-]{1,5}(?> [.-]{1,5})*)*',msg)
        print(matchObj.groups())
    else:
        for char in msg:
            print(CODE_OUT[char.upper()],)

if __name__ == "__main__":
    main()
