# test_convert.py
import pytest
from num_converter import convert
from num_converter import _symbol2number
from num_converter import _number2symbol

def test_for_self_equivalence_long(): # will not be passed on Python2 though
    assert convert("123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ", 62, 62) == "123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ123abcxyzABCXYZ"

#--------------- Boundary tests for internal _symbol2number() conversion/mapping function

def test_boundary_0():  # left bounary of ['0'..'9'] range
    assert _symbol2number('0') == 0

def test_boundary_9():  # right bounary of ['0'..'9'] range
    assert _symbol2number('9') == 9

def test_boundary_a():  # left bounary of ['a'..'z'] range
    assert _symbol2number('a') == 10

def test_boundary_z():  # right bounary of ['a'..'z'] range
    assert _symbol2number('z') == 35

def test_boundary_A():  # left bounary of ['A'..'Z'] range
    assert _symbol2number('A') == 36

def test_boundary_Z():  # right bounary of ['A'..'Z'] range
    assert _symbol2number('Z') == 61

def test_outofrange_before_0():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('0') - 1) )
    
def test_outofrange_after_9():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('9') + 1) )

def test_outofrange_before_a():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('a') - 1) )
    
def test_outofrange_after_z():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('z') + 1) )

def test_outofrange_before_A():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('A') - 1) )

def test_outofrange_after_Z():
    with pytest.raises(Exception):
        assert _symbol2number( char( ord('Z') + 1) )


#--------------- Boundary tests for internal _number2symbol() conversion/mapping function

def test_num2sym_boundary_0():
    assert _number2symbol(0) == '0'
    
def test_num2sym_boundary_9():
    assert _number2symbol(9) == '9'
    
def test_num2sym_boundary_10():
    assert _number2symbol(10) == 'a'
    
def test_num2sym_boundary_35():
    assert _number2symbol(35) == 'z'
    
def test_num2sym_boundary_36():
    assert _number2symbol(36) == 'A'
    
def test_num2sym_boundary_61():
    assert _number2symbol(61) == 'Z'
    
def test_num2sys_outofrange_before_0():
    with pytest.raises(Exception):
        assert _number2symbol(-1)

def test_num2sys_outofrange_after_61():
    with pytest.raises(Exception):
        assert _number2symbol(62)
        
    
# ---- argument values filtering

def test_empty_string():      
    with pytest.raises(Exception):
        convert("", 10, 10)
        
def test_wrong_arg1_type_notaString():
    with pytest.raises(Exception):
        convert(10, 62, 62)

def test_wrong_arg2_type_notAnInt():
    with pytest.raises(Exception):
        convert("abc", "abc", 62)

def test_wrong_arg3_type_notAnInt():
    with pytest.raises(Exception):
        convert("abc", 62, "abc")

def test_input_base_lower_than_min():
    with pytest.raises(Exception):
        convert("123", 1, 10)

def test_output_base_lower_than_min():
    with pytest.raises(Exception):
        convert("123", 10, 1)

def test_input_base_higher_than_max():
    with pytest.raises(Exception):
        convert("123", 63, 10)

def test_output_base_higher_than_max():
    with pytest.raises(Exception):
        convert("123", 10, 63)

def test_numsystem_base_mismatch(): # a string containing symbols that are not allowed for exact numeral system will raise an exception
    with pytest.raises(Exception):
        convert("123", 3, 10)       # Symbol '3' doesn't belong to allowed symbols for ternary numeral system

def test_preceding_zeroes():        # proves insensitivity to preceding '0' signs
    assert convert("00000123", 10, 10) == "123"


