#num_converter.py
# a module used to convert an integer number from given numeral system to desired
# Numeral system is defined by a natural number n | 2 <= n <= 62


def _symbol2number(c):
    # c: char
    # internal function used for mapping three intervals ['0'..'9'], ['a'..'z'], ['A'..'Z'] -> [0..61]
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    if c >= 'a' and c <= 'z':
        return (ord(c) - ord('a') + 10)
    if c >= 'A' and c <= 'Z':
        return (ord(c) - ord('A') + 36)
    else:
        raise Exception("Unsupported character in a string defining converted number")


def str2num(s, num_system):
    # s: str, num_system: int
    #check the arguments:
    if not (isinstance(s, str) and isinstance(num_system, int)):
        raise TypeError("Wrong argument type(s)")
    if num_system < 2 or num_system > 62:
        raise Exception("Requested numeral system must be an integer wihtin [2..62] range")
    if s == '':
        raise Exception("String defining a number should have non-zero length")
    
    n = 0                               # result
    multiplier = 1
    for i, c in enumerate(s[::-1]):
        converted = _symbol2number(c)
        if converted >= num_system:     # for example, if for binary system we received number 2, 3, etc instead of [0, 1]
            raise Exception("Char(s) in value-defining string does not match requested numeral system")
        n += converted * multiplier
        multiplier *= num_system    # just an optimized version of: " n += converted * num_system**i "
    return n


def _number2symbol(r):
    # r: integer
    # internal function used for mapping interval [0..61] -> ['0'..'9'], ['a'..'z'], ['A'..'Z']
    if r >= 0 and r <= 9:
        return chr(r + ord('0'))
    if r >= 10 and r <= 35:
        return chr(r + ord('a') - 10)
    if r >= 36 and r <= 61:
        return chr(r + ord('A') - 36)
    else:
        raise Exception("Argument should be within [0..61] range")


def num2str(a, num_system):
    # a: str, num_system: int
    # check the arguments:
    if not (isinstance(a, int) and isinstance(num_system, int)):
        raise TypeError("Wrong argument type(s)")
    if num_system < 2 or num_system > 62:
        raise Exception("Requested numeral system must be an integer wihtin [2..62] range")
    
    result = ''
    while a > 0:
        remainder = a % num_system
        a = a // num_system
        result = _number2symbol(remainder) + result
    return result


def convert(a, input_system, result_system):
    # a: str, input_system: int, result_system: int
    return num2str(str2num(a, input_system), result_system)
