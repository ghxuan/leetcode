def complex_number_multiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return number_to_complex(complex_to_numbers(a)*complex_to_numbers(b))


def complex_to_numbers(s):
    """
    :param s: str
    :return: complex
    """
    a, b = s.split('+')
    return int(a)+int(b.replace('i', ''))*1j


def number_to_complex(s):
    """
    :param s: complex
    :return: str
    """
    return f'{int(s.real)}+{int(s.imag)}i'


print(complex_number_multiply('1+1i', '1+1i'))
print(complex_number_multiply('1+-1i', '1+-1i'))
# 0+2i
# 0+-2i