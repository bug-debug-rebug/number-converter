#num_converter.py
# a module used to convert an integer number from given numeral system to desired
# Numeral system is defined by a natural number n | 2 <= n <= 62

def str2num(s, num_system):
    # s: str, num_system: int

    #check the arguments
    if not (isinstance(s, str) and isinstance(num_system, int)):
        raise TypeError("Wrong argument type(s)")
    if num_system < 2 or num_system > 62:
        raise Exception("Requested numeral system must be an integer wihtin [2..62] range")
    if s == '':
        raise Exception("String defining a number should have non-zero length")
    
    n = 0
    for i, c in enumerate(s[::-1]):
        if c >= '0' and c <= '9':
            converted = (ord(c) - ord('0'))
        elif c >= 'a' and c <= 'z':
            converted = (ord(c) - ord('a') + 10)
        elif c >= 'A' and c <= 'Z':
            converted = (ord(c) - ord('A') + 36)
        else:
            raise Exception("Unsupported character in string defining a number")
        if converted >= num_system:
            raise Exception("Char(s) in value-defining string does not match requested numeral system")
        n += converted * num_system**i
    return n
    
def num2str(a, num_system):
    # a: str, num_system: int

    #check the arguments
    if not (isinstance(a, int) and isinstance(num_system, int)):
        raise TypeError("Wrong argument type(s)")
    if num_system < 2 or num_system > 62:
        raise Exception("Requested numeral system must be an integer wihtin [2..62] range")
    
    res = ''
    while a > 0:
        r = a % num_system
        a = a // num_system
        if r <= 9:
            res = chr(r + ord('0')) + res
        elif r >= 10 and r <= 35:
            res = chr(r + ord('a') - 10) + res
        elif r >= 36:
            res = chr(r + ord('A') - 36) + res
    return res

def convert(a, input_system, result_system):
    # a: str, input_system: int, result_system: int
    return num2str(str2num(a, input_system), result_system)
    