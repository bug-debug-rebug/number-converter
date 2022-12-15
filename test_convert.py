# test_convert.py
import pytest
from num_converter import convert

def test_for_repeating():
    assert convert("123abcxyzABCXYZ", 62, 62) == "123abcxyzABCXYZ"

def test_for_repeating_long():
    assert convert("123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ", 62, 62) == "123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ"

def test_conversion_accuracy():
    assert convert("11111111", 2, 10) == "255"
    assert convert("11111111", 2, 10) == "255"
    assert convert("255", 10, 2) == "11111111"
    assert convert("255", 10, 16) == "ff"
    assert convert("ff", 16, 2) == "11111111"
    assert convert("ff", 16, 10) == "255"
    assert convert("1234567890abcdef", 16, 10) == "1311768467294899695"
    assert convert("1311768467294899695", 10, 16) == "1234567890abcdef"

def test_wrong_symbols_in_value_string():
    with pytest.raises(Exception):
        convert(" 123", 10, 10)
    with pytest.raises(Exception):
        convert("123.", 10, 10)

def test_value_vs_base_mismatch():
    with pytest.raises(Exception):
        convert("123", 3, 10)       # 3 lies out of ternary numeral system
        convert("1ZZ", 61, 10)      # Z lies out of 61-ary numeral syster
    
def test_empty_value_string():
    with pytest.raises(Exception):
        convert("", 10, 10)
        
def test_arguments_type():
    with pytest.raises(Exception):
        convert(12, 10, 10)
    with pytest.raises(Exception):
        convert(10, "12", 10)
    with pytest.raises(Exception):
        convert(10, 10, "12")

def test_base_lower_than_range():
    with pytest.raises(Exception):
        convert("123", 1, 10)
    with pytest.raises(Exception):
        convert("123", 10, 1)

def test_base_higher_than_range():
    with pytest.raises(Exception):
        convert("123", 63, 10)
    with pytest.raises(Exception):
        convert("123", 10, 63)

def test_minmax_values():
    assert convert("123", 62, 62) == "123"
    assert convert("101010", 2, 2) == "101010"

def test_preceding_zeroes():
    assert convert("00000123", 10, 10) == "123"
