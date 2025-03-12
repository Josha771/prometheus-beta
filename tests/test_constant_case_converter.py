import pytest
from src.constant_case_converter import to_constant_case

def test_to_constant_case_basic_strings():
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("helloWorld") == "HELLO_WORLD"
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"
    assert to_constant_case("hello_world") == "HELLO_WORLD"
    assert to_constant_case("hello-world") == "HELLO_WORLD"

def test_to_constant_case_complex_strings():
    assert to_constant_case("thisIsATestString") == "THIS_IS_A_TEST_STRING"
    assert to_constant_case("ThisIsATestString") == "THIS_IS_A_TEST_STRING"
    assert to_constant_case("this_is_a_test_string") == "THIS_IS_A_TEST_STRING"
    assert to_constant_case("this-is-a-test-string") == "THIS_IS_A_TEST_STRING"

def test_to_constant_case_edge_cases():
    assert to_constant_case("") == ""
    assert to_constant_case("a") == "A"
    assert to_constant_case("A") == "A"
    assert to_constant_case("  hello  world  ") == "HELLO_WORLD"

def test_to_constant_case_with_numbers():
    assert to_constant_case("hello2World") == "HELLO_2_WORLD"
    assert to_constant_case("hello_2_world") == "HELLO_2_WORLD"

def test_to_constant_case_error_handling():
    with pytest.raises(TypeError):
        to_constant_case(None)
    with pytest.raises(TypeError):
        to_constant_case(123)
    with pytest.raises(TypeError):
        to_constant_case(["hello"])