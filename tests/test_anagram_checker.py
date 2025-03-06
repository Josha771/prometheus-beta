import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_case_insensitive():
    """Test case-insensitive anagram detection"""
    assert are_anagrams("Astronomer", "Moon starer") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test anagram detection with whitespace"""
    assert are_anagrams("rail safety", "fairy tales") == True
    assert are_anagrams(" rail safety ", "fairy tales") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
    with pytest.raises(TypeError):
        are_anagrams("abc", None)
    with pytest.raises(TypeError):
        are_anagrams(["a"], ["b"])

def test_unicode_characters():
    """Test anagram detection with unicode characters"""
    assert are_anagrams("élément", "element") == True
    assert are_anagrams("café", "face") == False